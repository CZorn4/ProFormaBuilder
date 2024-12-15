import yfinance as yf
from datetime import datetime

def get_long_term_growth_rate():

    try:
        treasury = yf.Ticker("^TNX")
        growth_rate = treasury.info['regularMarketPrice'] / 100  # Convert basis points to decimal
        return min(growth_rate, 0.05)  # Cap at 5% to be conservative
    except:
        return 0.03  # Fallback to 3% if unable to fetch

def calculate_present_value(future_value, discount_rate, years):

    return future_value / ((1 + discount_rate) ** years)

def calculate_terminal_value(final_fcf, wacc, growth_rate):

    return final_fcf * (1 + growth_rate) / (wacc - growth_rate)

def calculate_valuation(fcf_data, wacc_data, shares_outstanding, financial_data):
    wacc = wacc_data['wacc']
    growth_rate = get_long_term_growth_rate()
    
    results = {
        'present_values': {},
        'valuation_summary': {}
    }
    
    # Get sorted years for sequential processing
    projected_years = sorted(fcf_data['years'].keys())
    base_year = min(projected_years)
    
    # Calculate present value of each projected FCF
    total_pv_fcf = 0
    for year in projected_years:
        fcf = fcf_data['years'][year]['fcf_calculation']['free_cash_flow']['value']
        years_out = int(year) - int(base_year)
        pv = calculate_present_value(fcf, wacc, years_out)
        
        results['present_values'][year] = {
            'fcf': fcf,
            'present_value': pv,
            'years_out': years_out,
            'date': f"{year}-12-31"
        }
        total_pv_fcf += pv
    
    # Calculate terminal value and its present value
    final_year = max(projected_years)
    final_fcf = fcf_data['years'][final_year]['fcf_calculation']['free_cash_flow']['value']
    terminal_value = calculate_terminal_value(final_fcf, wacc, growth_rate)
    years_to_terminal = int(final_year) - int(base_year)
    pv_terminal = calculate_present_value(terminal_value, wacc, years_to_terminal)
    
    # Get latest cash and debt from the most recent historical financial data
    historical_years = sorted(financial_data['years'].keys(), reverse=True)
    latest_year = historical_years[0]
    
    latest_cash = financial_data['years'][latest_year]['balance_sheet'].get('cash_and_securities', {}).get('value', 0)
    latest_debt = financial_data['years'][latest_year]['balance_sheet'].get('total_liabilities', {}).get('value', 0)
    
    # Calculate enterprise and equity values
    enterprise_value = total_pv_fcf + pv_terminal
    equity_value = enterprise_value + latest_cash - latest_debt
    
    # Store valuation summary
    results['valuation_summary'] = {
        'wacc': wacc,
        'long_term_growth_rate': growth_rate,
        'terminal_value': terminal_value,
        'pv_terminal_value': pv_terminal,
        'pv_fcf_total': total_pv_fcf,
        'enterprise_value': enterprise_value,
        'cash_and_securities': latest_cash,
        'total_liabilities': latest_debt,
        'equity_value': equity_value,
        'shares_outstanding': shares_outstanding,
        'equity_value_per_share': equity_value / shares_outstanding if shares_outstanding else None
    }
    
    return results