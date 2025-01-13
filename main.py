import argparse
from pro_forma_builder import ProFormaBuilder

def main():
    parser = argparse.ArgumentParser(description='Fetch and display financial statements from SEC filings.')
    parser.add_argument('ticker', type=str, help='Stock ticker symbol')
    
    # Change from years/quarters to basic/detailed
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('--basic', type=int, help='Number of years of basic financial data to fetch')
    mode_group.add_argument('--detailed', type=int, help='Number of years of detailed (including quarterly) financial data to fetch')
    
    parser.add_argument('--project', type=int, default=5, help='Number of years to project (default: 5)')
    parser.add_argument('--export', action='store_true', help='Export financial analysis to Excel')
    parser.add_argument('--output', type=str, default='financial_analysis.xlsx', help='Output filename for Excel export')
    parser.add_argument('--advanced', action='store_true', help='Enable advanced data collection for better WACC/valuation estimates')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode with additional output')
    parser.add_argument('--print', action='store_true', help='Enable print mode')
    
    args = parser.parse_args()
    
    # Update report type based on basic/detailed
    report_type = 'basic' if args.basic else 'detailed'
    period_count = args.basic if args.basic else args.detailed
    
    print(f"Fetching {period_count} years of {report_type} financial data for {args.ticker}...")
    
    builder = ProFormaBuilder(
        ticker=args.ticker,
        report_type=report_type,
        period_count=period_count,
        projection_years=args.project,
        advanced=args.advanced,
        debug=args.debug,
        print_mode=args.print
    )
    
    results = builder.build()
    
    if results is None:
        print("Failed to fetch financial data")
        return
    
    print("Analysis complete!")

if __name__ == "__main__":
    main()