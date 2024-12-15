from typing import Dict

def print_financial_statements(data, is_projection=False):
    
    # Define the order for income statement items
    income_statement_order = [
        'revenue',
        'cost_of_goods_sold',
        'interest_paid',
        'interest_earned',
        'depreciation',
        'profit_before_tax',
        'income_tax_expense',
        'profit_after_tax',
        'dividends'  # Removed retained_earnings from here
    ]
    
    # Define order for balance sheet items
    balance_sheet_order = [
        'cash_and_securities',
        'total_current_assets',
        'ppe_gross',
        'accumulated_depreciation',
        'ppe_net',
        'total_assets',
        'current_liabilities',
        'total_liabilities',
        'outstanding_stock',
        'StockHolders_Equity',
        'retained_earnings',  # Moved here between StockHolders_Equity and total_liabilities_and_SE
        'total_liabilities_and_SE'
    ]

    statement_type = "PROJECTED" if is_projection else "HISTORICAL"
    
    for year, statements in sorted(data['years'].items()):
        print(f"\n{statement_type} FINANCIAL STATEMENTS FOR YEAR {year}")
        print("=" * 70)
        
        print("\nINCOME STATEMENT")
        print("-" * 70)
        print(f"{'ITEM':<35} {'VALUE':>15} {'DATE':>15}")
        print("-" * 70)
        for item in income_statement_order:
            if item in statements['income_statement']:
                details = statements['income_statement'][item]
                print(f"{item.replace('_', ' ').title():<35} ${details['value']:>14,.2f} {details['date']}")
        
        print("\nBALANCE SHEET")
        print("-" * 70)
        print(f"{'ITEM':<35} {'VALUE':>15} {'DATE':>15}")
        print("-" * 70)
        for item in balance_sheet_order:
            if item in statements['balance_sheet']:
                details = statements['balance_sheet'][item]
                print(f"{item.replace('_', ' ').title():<35} ${details['value']:>14,.2f} {details['date']}")
        
        print("\n" + "=" * 70)

def print_ratio_statements(ratio_data):

    # Define the order of ratio items
    ratio_order = [
        'revenue_growth_rate',
        'current_assets_to_revenue',
        'current_liabilities_to_revenue',
        'net_fixed_assets_to_revenue',
        'operating_costs_to_revenue',
        'depreciation_rate',
        'interest_rate',
        'interest_paid_rate',
        'tax_rate',
        'dividend_growth_rate'
    ]
    
    for year, statements in sorted(ratio_data['years'].items()):
        print(f"\nFINANCIAL RATIOS FOR YEAR {year}")
        print("=" * 70)
        print(f"{'RATIO':<35} {'VALUE':>15} {'DATE':>15}")
        print("-" * 70)
        
        for item in ratio_order:
            if item in statements['ratios']:
                details = statements['ratios'][item]
                # Format ratio as percentage if it's a rate
                if 'rate' in item:
                    print(f"{item.replace('_', ' ').title():<35} {details['value']:>14.2%} {details['date']}")
                else:
                    print(f"{item.replace('_', ' ').title():<35} {details['value']:>14.4f} {details['date']}")
        
        print("\n" + "=" * 70)

def print_fcf_statements(fcf_data):

    # Define the order of FCF calculation items
    fcf_order = [
        'profit_after_tax',
        'add_back_depreciation',
        'subtract_increase_in_current_assets',
        'add_back_increase_in_current_liabilities',
        'subtract_increase_in_fixed_assets',
        'add_back_after_tax_interest_on_debt',
        'subtract_after_tax_interest_on_cash',
        'free_cash_flow'
    ]
    
    for year, statements in sorted(fcf_data['years'].items()):
        print(f"\nFREE CASH FLOW CALCULATION FOR YEAR {year}")
        print("=" * 70)
        print(f"{'ITEM':<35} {'VALUE':>15} {'DATE':>15}")
        print("-" * 70)
        
        for item in fcf_order:
            if item in statements['fcf_calculation']:
                details = statements['fcf_calculation'][item]
                print(f"{item.replace('_', ' ').title():<35} ${details['value']:>14,.2f} {details['date']}")
        
        print("\n" + "=" * 70)

def print_wacc_analysis(wacc_data):

    print("\nWACC ANALYSIS")
    print("=" * 70)
    print(f"{'COMPONENT':<35} {'VALUE':>15}")
    print("-" * 70)
    
    # Define order of WACC components
    wacc_order = [
        'beta',
        'r_squared',
        'risk_free_rate',
        'market_risk_premium',
        'cost_of_equity',
        'cost_of_debt',
        'tax_rate',
        'debt_weight',
        'equity_weight',
        'wacc'
    ]
    
    for item in wacc_order:
        if item in wacc_data:
            value = wacc_data[item]
            if any(rate in item for rate in ['rate', 'weight', 'wacc']):
                print(f"{item.replace('_', ' ').title():<35} {value:>14.2%}")
            else:
                print(f"{item.replace('_', ' ').title():<35} {value:>14.4f}")
    
    print("=" * 70)

def print_valuation_analysis(valuation_data):
    # Print present values of projected cash flows
    print("\nPRESENT VALUE CALCULATIONS")
    print("=" * 70)
    print(f"{'YEAR':<10} {'FCF':>15} {'PV FACTOR':>12} {'PRESENT VALUE':>18}")
    print("-" * 70)
    
    for year, pv_data in sorted(valuation_data['present_values'].items()):
        fcf = pv_data['fcf']
        pv = pv_data['present_value']
        pv_factor = pv / fcf if fcf != 0 else 0
        
        print(f"{year:<10} ${fcf:>14,.2f} {pv_factor:>11.4f} ${pv:>17,.2f}")
    
    print("\nVALUATION SUMMARY")
    print("=" * 70)
    print(f"{'COMPONENT':<35} {'VALUE':>15}")
    print("-" * 70)
    
    summary = valuation_data['valuation_summary']
    metrics = [
        ('WACC', summary['wacc'], True),
        ('Long Term Growth Rate', summary['long_term_growth_rate'], True),
        ('Present Value of FCF', summary['pv_fcf_total'], False),
        ('Terminal Value', summary['terminal_value'], False),
        ('PV of Terminal Value', summary['pv_terminal_value'], False),
        ('Enterprise Value', summary['enterprise_value'], False),
        ('Cash and Securities', summary['cash_and_securities'], False),
        ('Total Liabilities', summary['total_liabilities'], False),
        ('Equity Value', summary['equity_value'], False),
        ('Shares Outstanding', summary['shares_outstanding'], False)
    ]
    
    for label, value, is_percent in metrics:
        if label == 'Shares Outstanding':
            print(f"{label:<35} {value:>14,}")
        elif is_percent:
            print(f"{label:<35} {value:>14.2%}")
        else:
            print(f"{label:<35} ${value:>14,.2f}")
    
    if summary['equity_value_per_share']:
        print(f"{'Equity Value per Share':<35} ${summary['equity_value_per_share']:>14,.2f}")
    
    print("=" * 70)