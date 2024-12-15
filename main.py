from sec_data import extract_financial_data
from display import print_financial_statements, print_ratio_statements, print_fcf_statements, print_wacc_analysis, print_valuation_analysis
from calcratios import calculate_ratios
from forecast import project_financial_statements, calculate_historical_averages
from valuation import calculate_valuation
from calcfcf import calculate_fcf
from wacc import calculate_wacc
from excelexport import export_financial_analysis_to_excel
import argparse


def print_projection_ratios(averages):
    print("\nRATIOS USED FOR PROJECTIONS")
    print("=" * 70)
    print(f"{'RATIO':<35} {'VALUE':>15}")
    print("-" * 70)

    for ratio, value in averages.items():
        if isinstance(value, float):  # Only print numeric ratios
            if 'rate' in ratio:
                print(f"{ratio.replace('_', ' ').title():<35} {value:>14.2%}")
            else:
                print(f"{ratio.replace('_', ' ').title():<35} {value:>14.4f}")
    print("=" * 70)

def main():
    # Updated CL config
    parser = argparse.ArgumentParser(description='Fetch and display financial statements from SEC filings.')
    parser.add_argument('ticker', type=str, help='Stock ticker symbol')
    parser.add_argument('--years', type=int, default=1, help='Number of years of data to fetch (default: 1)')
    parser.add_argument('--project', type=int, default=5, help='Number of years to project (default: 5)')
    parser.add_argument('--export', action='store_true', help='Export financial analysis to Excel')
    parser.add_argument('--output', type=str, default='financial_analysis.xlsx', help='Output filename for Excel export (default: financial_analysis.xlsx)')
    
    args = parser.parse_args()
    
    print(f"Fetching {args.years} years of financial data for {args.ticker}...")
    
    financial_data = extract_financial_data(args.ticker, args.years)
    if financial_data:
        print_financial_statements(financial_data)
        
        # Calculate and display ratios
        ratio_data = calculate_ratios(financial_data)
        print_ratio_statements(ratio_data)
        
        # Generate and display projections
        projected_data = None
        fcf_data = None
        wacc_data = None
        valuation_results = None
        
        if args.project > 0:
            print(f"\nGenerating {args.project} year projection...")
            
            # First calculate and display the ratios being used
            averages = calculate_historical_averages(financial_data, ratio_data)
            print_projection_ratios(averages)
            
            # Then generate projections
            projected_data = project_financial_statements(financial_data, ratio_data, args.project)
            print_financial_statements(projected_data, is_projection=True)
            
            # Calculate and display FCF for projected years
            fcf_data = calculate_fcf(projected_data, financial_data)
            print_fcf_statements(fcf_data)

            # calc wacc
            shares_outstanding = financial_data.get('shares_outstanding', 1)
            wacc_data = calculate_wacc(args.ticker, financial_data, ratio_data)
            print_wacc_analysis(wacc_data)

            # final val
            valuation_results = calculate_valuation(fcf_data, wacc_data, shares_outstanding, financial_data)
            print_valuation_analysis(valuation_results)
        
        # Excel export option
        if args.export and projected_data and fcf_data and wacc_data and valuation_results:
            export_financial_analysis_to_excel(
                financial_data, 
                ratio_data, 
                projected_data, 
                fcf_data, 
                wacc_data, 
                valuation_results, 
                args.output
            )
    else:
        print("Failed to fetch financial data")

if __name__ == "__main__":
    main()