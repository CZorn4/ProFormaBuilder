from sec_data import extract_financial_data
from display import print_financial_statements
import argparse

def main():
    # small CL config
    parser = argparse.ArgumentParser(description='Fetch and display financial statements from SEC filings.')
    parser.add_argument('ticker', type=str, help='Stock ticker symbol')
    parser.add_argument('--years', type=int, default=1, help='Number of years of data to fetch (default: 1)')
    
    args = parser.parse_args()
    
    print(f"Fetching {args.years} years of financial data for {args.ticker}...")
    
    financial_data = extract_financial_data(args.ticker, args.years)
    if financial_data:
        print_financial_statements(financial_data)
    else:
        print("Failed to fetch financial data")

if __name__ == "__main__":
    main()