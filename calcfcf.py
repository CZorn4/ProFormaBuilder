def calculate_fcf(projected_data, financial_data):

    results = {
        'years': {}
    }
    
    # Get the last historical year's data to use as base year
    historical_years = sorted(financial_data['years'].keys())
    last_historical_year = historical_years[-1]
    last_historical_data = financial_data['years'][last_historical_year]
    
    # Process each projected year
    projected_years = sorted(projected_data['years'].keys())
    for i in range(len(projected_years)):
        current_year = projected_years[i]
        year_data = projected_data['years'][current_year]
        
        # For first projected year, use base year (last historical) as previous
        if i == 0:
            prev_year_data = last_historical_data
        else:
            prev_year = projected_years[i-1]
            prev_year_data = projected_data['years'][prev_year]
        
        results['years'][current_year] = {
            'fcf_calculation': {}
        }
        
        # Start with profit after tax
        profit_after_tax = year_data['income_statement']['profit_after_tax']['value']
        results['years'][current_year]['fcf_calculation']['profit_after_tax'] = {
            'value': profit_after_tax,
            'date': f"{current_year}-12-31"
        }
        
        # Add back depreciation
        depreciation = year_data['income_statement']['depreciation']['value']
        results['years'][current_year]['fcf_calculation']['add_back_depreciation'] = {
            'value': depreciation,
            'date': f"{current_year}-12-31"
        }
        
        # Calculate changes in working capital components
        # Change in current assets
        current_assets_change = (
            year_data['balance_sheet']['total_current_assets']['value'] -
            prev_year_data['balance_sheet']['total_current_assets']['value']
        )
        results['years'][current_year]['fcf_calculation']['subtract_increase_in_current_assets'] = {
            'value': -current_assets_change,
            'date': f"{current_year}-12-31"
        }
        
        # Change in current liabilities
        current_liab_change = (
            year_data['balance_sheet']['current_liabilities']['value'] -
            prev_year_data['balance_sheet']['current_liabilities']['value']
        )
        results['years'][current_year]['fcf_calculation']['add_back_increase_in_current_liabilities'] = {
            'value': current_liab_change,
            'date': f"{current_year}-12-31"
        }
        
        # Change in fixed assets at cost (PPE Gross)
        fixed_assets_change = (
            year_data['balance_sheet']['ppe_gross']['value'] -
            prev_year_data['balance_sheet']['ppe_gross']['value']
        )
        results['years'][current_year]['fcf_calculation']['subtract_increase_in_fixed_assets'] = {
            'value': -fixed_assets_change,
            'date': f"{current_year}-12-31"
        }
        
        # Add back after-tax interest on debt
        interest_paid = year_data['income_statement']['interest_paid']['value']
        tax_rate = abs(year_data['income_statement']['income_tax_expense']['value'] / 
                      year_data['income_statement']['profit_before_tax']['value'])
        after_tax_interest = interest_paid * (1 - tax_rate)
        results['years'][current_year]['fcf_calculation']['add_back_after_tax_interest_on_debt'] = {
            'value': after_tax_interest,
            'date': f"{current_year}-12-31"
        }
        
        # Subtract after-tax interest on cash
        interest_earned = year_data['income_statement']['interest_earned']['value']
        after_tax_interest_earned = interest_earned * (1 - tax_rate)
        results['years'][current_year]['fcf_calculation']['subtract_after_tax_interest_on_cash'] = {
            'value': -after_tax_interest_earned,
            'date': f"{current_year}-12-31"
        }
        
        # Calculate FCF
        fcf = (profit_after_tax + depreciation + 
               (results['years'][current_year]['fcf_calculation']['subtract_increase_in_current_assets']['value']) +
               (results['years'][current_year]['fcf_calculation']['add_back_increase_in_current_liabilities']['value']) +
               (results['years'][current_year]['fcf_calculation']['subtract_increase_in_fixed_assets']['value']) +
               after_tax_interest - after_tax_interest_earned)
        
        results['years'][current_year]['fcf_calculation']['free_cash_flow'] = {
            'value': fcf,
            'date': f"{current_year}-12-31"
        }
    
    return results