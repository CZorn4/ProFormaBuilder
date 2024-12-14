from typing import Dict

def print_financial_statements(data):
    
    # Define the order for income statement items
    income_statement_order = [
        'revenue',
        'cost_of_goods_sold',
        'interest_paid',
        'interest_earned',
        'depreciation',
        'profit_before_tax',
        'income_tax',
        'profit_after_tax',
        'retained_earnings'
    ]
    
    # Define order for balance sheet items
    balance_sheet_order = [
        'cash_and_securities',
        'current_assets',
        'ppe_gross',
        'accumulated_depreciation',
        'ppe_net',
        'current_liabilities',
        'retained_earnings',
        'StockHolders Equity'
    ]

    for year, statements in sorted(data['years'].items()):
        print(f"\nFINANCIAL STATEMENTS FOR YEAR {year}")
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