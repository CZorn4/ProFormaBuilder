from utils.http_client import make_http_request
from xbrl_tags import get_xbrl_tags
from financial_structure import get_financial_structure
from utils.printer import ProFormaPrinter
import pandas as pd

class ProFormaBuilder:
    def __init__(self, ticker, report_type, period_count, projection_years=5, advanced=False, debug=False, print_mode=False):
        self.ticker = ticker
        self.cik = None
        if report_type not in ['basic', 'detailed']:
            raise ValueError("report_type must be either 'basic' or 'detailed'")
        self.report_type = report_type
        self.period_count = period_count
        self.projection_years = projection_years
        self.advanced = advanced
        self.debug = debug
        self.print_enabled = print_mode
        
        self.xbrl_tags = get_xbrl_tags()
        self.financial_structure = get_financial_structure()
        
        if self.print_enabled:
            self.printer = ProFormaPrinter(xbrl_tags=self.xbrl_tags, 
                                         financial_structure=self.financial_structure,
                                         debug=debug)
        self.end_dates = None
        self.financial_data = None
        self.ratio_data = None
        self.projected_data = None
        self.fcf_data = None
        self.wacc_data = None
        self.valuation_results = None

        if self.debug:
            print(f"Debug mode enabled")
            print(f"Initialization parameters:")
            print(f"  Ticker: {self.ticker}")
            print(f"  Report Type: {self.report_type}")
            print(f"  Period Count: {self.period_count}")
            print(f"  Projection Years: {self.projection_years}")
            print(f"  Advanced Mode: {self.advanced}")
            print(f"  Print Mode: {self.print_enabled}")

    def debug_print(self, message):
        if self.debug:
            print(f"[DEBUG] {message}")

    def convert_ticker_to_cik(self):
        self.debug_print("Starting convert_ticker_to_cik()...")
        cik_url = "https://www.sec.gov/files/company_tickers.json"
        
        response = make_http_request(url=cik_url)
        if not response:
            self.debug_print("Failed to get response from SEC ticker database")
            return None
            
        try:
            company_data = response.json()
            ticker = self.ticker.upper()
            
            for company in company_data.values():
                if company['ticker'] == ticker:
                    self.cik = str(company['cik_str']).zfill(10)
                    self.debug_print(f"Found CIK: {self.cik}")
                    return self.cik
                    
            self.debug_print(f"No CIK found for ticker {ticker}")
            return None
        except Exception as e:
            self.debug_print(f"Error processing company data: {e}")
            return None
    
    def fetch_data(self):
        self.debug_print(f"Fetching {self.period_count} of financial data for {self.ticker}...")
        
        try:
            response = make_http_request(cik=self.cik)
            if not response:
                self.debug_print("Failed to get response from SEC API")
                return
                
            self.financial_data = response.json()
            self.debug_print(f"Successfully fetched data for CIK: {self.cik}")
            
        except Exception as e:
            self.debug_print(f"Error fetching data: {e}")
            return
    
    def get_target_end_dates(self):
        url = f'https://data.sec.gov/submissions/CIK{self.cik}.json'
        response = make_http_request(url)
        data = response.json()

        self.debug_print("Getting recent filings...")
        df_recent = pd.DataFrame(data['filings']['recent'])
        self.debug_print(f"Found {len(df_recent)} recent filings")

        older_files = data['filings'].get('files', [])
        self.debug_print(f"Found {len(older_files)} older file sets")
        
        if older_files:
            for file in older_files:
                old_url = f"https://data.sec.gov/submissions/{file['name']}"
                response = make_http_request(old_url)
                old_data = response.json()
                df_older = pd.DataFrame(old_data)
                df_recent = pd.concat([df_recent, df_older], ignore_index=True)
        
        self.debug_print(f"Total filings before filter: {len(df_recent)}")
        self.debug_print(f"Unique forms: {df_recent['form'].unique()}")
        self.debug_print(f"XBRL values: {df_recent['isXBRL'].unique()}")
        
        # only keep the filings set up with XBRL
        filings = df_recent[
            (df_recent['form'].isin(['10-K', '10-Q'])) & 
            (df_recent['isXBRL'] == 1) 
        ]

        self.debug_print(f"Found {len(filings)} qualifying filings")
        
        if filings.empty:
            self.debug_print("No XBRL data for company")
            return

        target_end_dates = {}
        annuals_seen = 0

        # Using itertuples() for better performance
        for filing in filings.itertuples():
            target_end_dates[filing.reportDate] = filing.form
            if filing.form == '10-K':
                annuals_seen += 1
                if annuals_seen >= self.period_count:
                    break
        
        self.debug_print(f"Found {len(target_end_dates)} target end dates")
        self.debug_print(f"Target dates: {list(target_end_dates.keys())}")

        if self.report_type == 'basic':
            filtered_dates = {}
            for date, form in target_end_dates.items():
                if form == '10-K':
                    filtered_dates[date] = form
            self.end_dates = filtered_dates
        else:
            self.end_dates = target_end_dates

        self.debug_print(f"Final end dates: {list(self.end_dates.keys())}")
                
    def get_line_items(self):
        """
        Get line items for each target end date from company facts.
        Returns a dictionary with end dates as keys containing financial data.
        Each line item contains the value, end date, and frame information.
        """
        self.debug_print("Starting get_line_items()...")
        
        # First check if we have the required data to proceed
        if not self.financial_data or not self.end_dates:
            self.debug_print("Missing required financial data or end dates")
            return None
            
        financial_statements = {}
        
        # Initialize the results dictionary for each target end date
        for end_date in self.end_dates.keys():
            financial_statements[end_date] = {}
        
        try:
            # Get the us-gaap facts from the financial data
            facts = self.financial_data.get('facts', {}).get('us-gaap', {})
            if not facts:
                self.debug_print("No us-gaap facts found in financial data")
                return None
                
            # Process each financial concept we're looking for
            for concept, possible_tags in self.xbrl_tags.items():
                for end_date in self.end_dates.keys():
                    found_value = False
                    
                    # Try each possible XBRL tag for this concept
                    for tag in possible_tags:
                        if found_value:
                            break
                            
                        tag_data = facts.get(tag)
                        if not tag_data:
                            continue
                            
                        # Get the units data (typically 'USD' or 'shares')
                        units = tag_data.get('units', {})
                        for unit_values in units.values():
                            if found_value:
                                break
                            
                            # Find all entries matching our target end date
                            matching_entries = [
                                v for v in unit_values 
                                if v.get('end') == end_date
                            ]

                            if matching_entries:
                                selected_value = None
                                
                                if len(matching_entries) == 1:
                                    # If only one entry exists, use it regardless of frame
                                    selected_value = matching_entries[0]
                                else:
                                    # For multiple entries, prefer ones with frames
                                    entries_with_frames = [
                                        v for v in matching_entries 
                                        if v.get('frame') is not None
                                    ]
                                    
                                    if entries_with_frames:
                                        # Use the last entry that has a frame
                                        selected_value = entries_with_frames[-1]
                                    else:
                                        # If no entries have frames, use the last entry
                                        selected_value = matching_entries[-1]
                                
                                # Store the selected value if we found one
                                if selected_value:
                                    financial_statements[end_date][concept] = {
                                        'value': selected_value.get('val'),
                                        'end': selected_value.get('end'),
                                        'start': selected_value.get('start'),
                                        'frame': selected_value.get('frame'),
                                        'tag': tag
                                    }
                                    found_value = True
                    
                    # Only log if we completely failed to find a value for this concept
                    if not found_value:
                        financial_statements[end_date][concept] = {
                            'value': None,
                            'end': end_date,
                            'start': None,
                            'frame': None,
                            'tag': None
                        }
                        self.debug_print(f"No value found for {concept} on {end_date}")
        
        except Exception as e:
            self.debug_print(f"Error processing line items: {e}")
            return None
        
        self.financial_statements = financial_statements
        return financial_statements
    
    def build(self):
        """
        Main method to build financial analysis
        """
        self.debug_print("Starting build process...")
        
        # Step 1: Convert ticker to CIK
        if not self.convert_ticker_to_cik():
            self.debug_print("Failed to convert ticker to CIK")
            return None
            
        # Step 2: Fetch data
        self.fetch_data()
        if not self.financial_data:
            self.debug_print("Failed to fetch financial data")
            return None
            
        # Step 3: Get target end dates
        self.get_target_end_dates()
        if not self.end_dates:
            self.debug_print("Failed to get target end dates")
            return None
            
        # Step 4: Get line items
        self.get_line_items()
        if not self.financial_statements:
            self.debug_print("Failed to get line items")
            return None
            
        # Step 5: Print if enabled
        if self.print_enabled:
            self.printer.print_financial_statements(self.financial_statements)
            
        return self.financial_statements