import requests
from ticker_to_cik import get_cik_from_ticker
from xbrl_tags import get_xbrl_tags

def get_sec_data(ticker):

    headers = {
        'User-Agent': 'Collin Zorn collin.d.zorn-1@ou.edu'
    }
    
    cik = get_cik_from_ticker(ticker)
    if not cik:
        return None
    
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def get_historical_10k_values(data_array, tag_name=None, desired_years=1):

    ten_k_entries = [entry for entry in data_array if entry.get('form') == '10-K']
    
    # Group entries by year
    entries_by_year = {}
    for entry in ten_k_entries:
        year = entry['end'][:4]  # Get the year part of the date
        if year not in entries_by_year:
            entries_by_year[year] = []
        entries_by_year[year].append(entry)
    
    # IMPORTANT: There are multiple filings under 10-k for some/most years. I am pretty sure this is because
    # the company made a "revision" filing and for some reason this is still under 10-k. This genius
    # architecture is what allows there to be blank line items for line items that shouldnt be blank,
    # becasue any item not re-recorded in the revision will return blank. So, we dig through the 0's
    # until we find a non-zero, and then record that. this took way too long to figure out.
    results = []
    for year in sorted(entries_by_year.keys(), reverse=True):
        year_entries = entries_by_year[year]
        # Sort entries for this year by date, latest first
        year_entries.sort(key=lambda x: x['end'], reverse=True)
        
        # Find the latest valid value
        value = None
        date = None
        for entry in year_entries:
            if entry['val'] != 0:  # Skip zero values
                value = entry['val']
                date = entry['end']
                break
        
        if value is not None:
            # Tax benefits are encompassed in (parenthesis) even though they actually add to get net income
            # after taxes. Handle accordingly
            if tag_name in ['IncomeTaxExpenseBenefit', 'IncomeTaxesPaid']:
                if value < 0:
                    value = abs(value)
                else:
                    value = -value
            
            results.append((value, date))
            if len(results) >= desired_years:
                break
    
    return results

def extract_financial_data(ticker, desired_years=1):
    
    data = get_sec_data(ticker)
    if not data:
        return None
    
    mappings = get_xbrl_tags()
    
    # Initialize results structure for multiple years
    results = {
        'years': {}
    }
    
    # Process both statement types for each year
    for statement_type, tags in mappings.items():
        for item, possible_tags in tags.items():
            for tag in possible_tags:
                if tag in data['facts']['us-gaap']:
                    if 'USD' in data['facts']['us-gaap'][tag]['units']:
                        values = get_historical_10k_values(
                            data['facts']['us-gaap'][tag]['units']['USD'],
                            tag,
                            desired_years
                        )
                        
                        # Store values for each year
                        for value, end_date in values:
                            year = end_date[:4]  # Extract year from date
                            if year not in results['years']:
                                results['years'][year] = {
                                    'income_statement': {},
                                    'balance_sheet': {}
                                }
                            results['years'][year][statement_type][item] = {
                                'value': value,
                                'date': end_date
                            }
                        break

    all_years = sorted(results['years'].keys(), reverse=True)
    years_to_keep = all_years[:desired_years]
    results['years'] = {year: results['years'][year] for year in years_to_keep}

    # Calculate depreciation from accumulated depreciation changes bc I cant figure out how to pull it
    sorted_years = sorted(results['years'].keys())
    for i in range(1, len(sorted_years)):
        current_year = sorted_years[i]
        prev_year = sorted_years[i-1]
        
        # Get accumulated depreciation values
        if ('accumulated_depreciation' in results['years'][current_year]['balance_sheet'] and 
            'accumulated_depreciation' in results['years'][prev_year]['balance_sheet']):
            current_acc_dep = results['years'][current_year]['balance_sheet']['accumulated_depreciation']['value']
            prev_acc_dep = results['years'][prev_year]['balance_sheet']['accumulated_depreciation']['value']
            
            # Calculate and store depreciation
            depreciation = current_acc_dep - prev_acc_dep
            results['years'][current_year]['income_statement']['depreciation'] = {
                'value': depreciation,
                'date': results['years'][current_year]['balance_sheet']['accumulated_depreciation']['date']
            }

    # Calculate profit before tax for each year
    for year in results['years']:
        if ('profit_after_tax' in results['years'][year]['income_statement'] and 
            'income_tax' in results['years'][year]['income_statement']):
            profit_after_tax = results['years'][year]['income_statement']['profit_after_tax']['value']
            income_tax = results['years'][year]['income_statement']['income_tax']['value']
            
            # Calculate profit before tax
            profit_before_tax = profit_after_tax + income_tax
            
            # Store with the same date as profit after tax
            results['years'][year]['income_statement']['profit_before_tax'] = {
                'value': profit_before_tax,
                'date': results['years'][year]['income_statement']['profit_after_tax']['date']
            }

    return results