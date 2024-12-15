def calculate_historical_averages(financial_data, ratio_data):
    
    averages = {}
    years = sorted(ratio_data['years'].keys())
    
    rate_sums = {
        'revenue_growth_rate': 0,
        'depreciation_rate': 0,
        'tax_rate': 0
    }
    rate_counts = {
        'revenue_growth_rate': 0,
        'depreciation_rate': 0,
        'tax_rate': 0
    }
    
    for year in years:
        year_ratios = ratio_data['years'][year]['ratios']
        
        for rate in rate_sums.keys():
            if rate in year_ratios:
                rate_sums[rate] += year_ratios[rate]['value']
                rate_counts[rate] += 1
    
    for rate in rate_sums.keys():
        if rate_counts[rate] > 0:
            averages[rate] = rate_sums[rate] / rate_counts[rate]
    
    base_year = years[-1]
    base_ratios = ratio_data['years'][base_year]['ratios']
    
    averages.update({
        'current_assets_to_revenue': base_ratios['current_assets_to_revenue']['value'],
        'current_liabilities_to_revenue': base_ratios['current_liabilities_to_revenue']['value'],
        'net_fixed_assets_to_revenue': base_ratios['net_fixed_assets_to_revenue']['value'],
        'operating_costs_to_revenue': base_ratios['operating_costs_to_revenue']['value'],
        'interest_rate': base_ratios['interest_rate']['value'],
        'interest_paid_rate': base_ratios['interest_paid_rate']['value']
    })
    
    base_year_data = financial_data['years'][base_year]
    averages['base_long_term_liabilities'] = (
        base_year_data['balance_sheet']['total_liabilities']['value'] -
        base_year_data['balance_sheet']['current_liabilities']['value']
    )
    averages['base_stockholders_equity'] = base_year_data['balance_sheet']['StockHolders_Equity']['value']
    averages['base_retained_earnings'] = base_year_data['balance_sheet'].get('retained_earnings', {'value': 0})['value']
    
    return averages

def project_financial_statements(financial_data, ratio_data, projection_years=5):
    
    averages = calculate_historical_averages(financial_data, ratio_data)
    base_year = max(financial_data['years'].keys())
    base_year_data = financial_data['years'][base_year]
    
    results = {
        'years': {}
    }
    
    for year_num in range(1, projection_years + 1):
        projection_year = str(int(base_year) + year_num)
        prev_year = str(int(projection_year) - 1)
        
        results['years'][projection_year] = {
            'income_statement': {},
            'balance_sheet': {}
        }
        
        year_data = results['years'][projection_year]
        prev_year_data = (results['years'][prev_year] if prev_year in results['years'] 
                         else financial_data['years'][prev_year])
        
        # Revenue projection remains the same
        prev_revenue = prev_year_data['income_statement']['revenue']['value']
        revenue = prev_revenue * (1 + averages['revenue_growth_rate'])
        year_data['income_statement']['revenue'] = {
            'value': revenue,
            'date': f"{projection_year}-12-31"
        }
        
        # Rest of income statement calculations
        year_data['income_statement']['cost_of_goods_sold'] = {
            'value': revenue * averages['operating_costs_to_revenue'],
            'date': f"{projection_year}-12-31"
        }
        
        # Balance sheet assets
        year_data['balance_sheet']['total_current_assets'] = {
            'value': revenue * averages['current_assets_to_revenue'],
            'date': f"{projection_year}-12-31"
        }
        
        year_data['balance_sheet']['ppe_net'] = {
            'value': revenue * averages['net_fixed_assets_to_revenue'],
            'date': f"{projection_year}-12-31"
        }
        
        # Liabilities
        year_data['balance_sheet']['current_liabilities'] = {
            'value': revenue * averages['current_liabilities_to_revenue'],
            'date': f"{projection_year}-12-31"
        }
        
        long_term_liabilities = averages['base_long_term_liabilities']
        year_data['balance_sheet']['total_liabilities'] = {
            'value': year_data['balance_sheet']['current_liabilities']['value'] + long_term_liabilities,
            'date': f"{projection_year}-12-31"
        }
        
        # Calculate all other income statement items needed for retained earnings
        prev_cash = prev_year_data['balance_sheet'].get('cash_and_securities', {'value': 0})['value']
        avg_liabilities = (prev_year_data['balance_sheet']['total_liabilities']['value'] + 
                         year_data['balance_sheet']['total_liabilities']['value']) / 2
        
        year_data['income_statement']['interest_paid'] = {
            'value': avg_liabilities * averages['interest_rate'],
            'date': f"{projection_year}-12-31"
        }
        
        if 'accumulated_depreciation' in prev_year_data['balance_sheet']:
            prev_accum_dep = prev_year_data['balance_sheet']['accumulated_depreciation']['value']
        else:
            prev_accum_dep = base_year_data['balance_sheet']['accumulated_depreciation']['value']
        
        year_data['income_statement']['depreciation'] = {
            'value': year_data['balance_sheet']['ppe_net']['value'] * averages['depreciation_rate'],
            'date': f"{projection_year}-12-31"
        }
        
        # Update accumulated depreciation
        year_data['balance_sheet']['accumulated_depreciation'] = {
            'value': prev_accum_dep + year_data['income_statement']['depreciation']['value'],
            'date': f"{projection_year}-12-31"
        }
        
        # Calculate profit before and after tax
        profit_before_tax = (
            year_data['income_statement']['revenue']['value'] -
            year_data['income_statement']['cost_of_goods_sold']['value'] -
            year_data['income_statement']['interest_paid']['value'] -
            year_data['income_statement']['depreciation']['value']
        )
        
        year_data['income_statement']['profit_before_tax'] = {
            'value': profit_before_tax,
            'date': f"{projection_year}-12-31"
        }
        
        tax_expense = profit_before_tax * averages['tax_rate']
        year_data['income_statement']['income_tax_expense'] = {
            'value': tax_expense,
            'date': f"{projection_year}-12-31"
        }
        
        profit_after_tax = profit_before_tax - tax_expense
        year_data['income_statement']['profit_after_tax'] = {
            'value': profit_after_tax,
            'date': f"{projection_year}-12-31"
        }
        
        # Calculate retained earnings
        prev_retained_earnings = (prev_year_data['balance_sheet'].get('retained_earnings', {'value': averages['base_retained_earnings']})['value'])
        year_data['balance_sheet']['retained_earnings'] = {
            'value': prev_retained_earnings + profit_after_tax,
            'date': f"{projection_year}-12-31"
        }
        
        # Update stockholders equity to include retained earnings
        year_data['balance_sheet']['StockHolders_Equity'] = {
            'value': averages['base_stockholders_equity'] + year_data['balance_sheet']['retained_earnings']['value'],
            'date': f"{projection_year}-12-31"
        }
        
        # Update total liabilities and stockholders equity
        total_liab_equity = (year_data['balance_sheet']['total_liabilities']['value'] + 
                           year_data['balance_sheet']['StockHolders_Equity']['value'])
        
        year_data['balance_sheet']['total_liabilities_and_SE'] = {
            'value': total_liab_equity,
            'date': f"{projection_year}-12-31"
        }
        
        # Calculate final cash position
        year_data['balance_sheet']['cash_and_securities'] = {
            'value': (total_liab_equity - 
                     year_data['balance_sheet']['total_current_assets']['value'] - 
                     year_data['balance_sheet']['ppe_net']['value']),
            'date': f"{projection_year}-12-31"
        }
        
        # Calculate interest earned based on average cash position
        avg_cash = (prev_cash + year_data['balance_sheet']['cash_and_securities']['value']) / 2
        year_data['income_statement']['interest_earned'] = {
            'value': avg_cash * averages['interest_paid_rate'],
            'date': f"{projection_year}-12-31"
        }
        
        # Update PPE gross value
        year_data['balance_sheet']['ppe_gross'] = {
            'value': (year_data['balance_sheet']['ppe_net']['value'] + 
                     year_data['balance_sheet']['accumulated_depreciation']['value']),
            'date': f"{projection_year}-12-31"
        }
    
    return results