def calculate_average(current_value, previous_value):

    if previous_value is not None:
        return (current_value + previous_value) / 2
    return None

def calculate_ratios(financial_data):

    results = {
        'years': {}
    }
    
    # Get sorted years for proper year-over-year calculations, identify final year for some calcs
    years = sorted(financial_data['years'].keys())
    first_year = years[0]
    final_year = years[-1]
    
    for i, year in enumerate(years):
        prev_year = years[i-1] if i > 0 else None
        year_data = financial_data['years'][year]
        
        # Initialize the ratios structure for this year
        results['years'][year] = {
            'ratios': {}
        }
        ratios = results['years'][year]['ratios']
        
        # Get values from financial statements. use get to prevent explosion TODO: 0's arent good either
        revenue = year_data['income_statement'].get('revenue', {}).get('value', 0)
        current_assets = year_data['balance_sheet'].get('total_current_assets', {}).get('value', 0)
        current_liabilities = year_data['balance_sheet'].get('current_liabilities', {}).get('value', 0)
        ppe_net = year_data['balance_sheet'].get('ppe_net', {}).get('value', 0)
        cogs = year_data['income_statement'].get('cost_of_goods_sold', {}).get('value', 0)
        depreciation = year_data['income_statement'].get('depreciation', {}).get('value', 0)
        interest_paid = year_data['income_statement'].get('interest_paid', {}).get('value', 0)
        total_liabilities = year_data['balance_sheet'].get('total_liabilities', {}).get('value', 0)
        profit_before_tax = year_data['income_statement'].get('profit_before_tax', {}).get('value', 0)
        profit_after_tax = year_data['income_statement'].get('profit_after_tax', {}).get('value', 0)
        dividends = year_data['income_statement'].get('dividends', {}).get('value', 0)
        cash_and_securities = year_data['balance_sheet'].get('cash_and_securities', {}).get('value', 0)
        
        # Calculate Revenue Growth Rate
        if prev_year:
            prev_year_revenue = financial_data['years'][prev_year]['income_statement'].get('revenue', {}).get('value', 0)
            if prev_year_revenue != 0:
                revenue_growth = (revenue - prev_year_revenue) / prev_year_revenue
                ratios['revenue_growth_rate'] = {
                    'value': revenue_growth,
                    'date': year_data['income_statement'].get('revenue', {}).get('date')
                }
        
        # Calculate Asset/Revenue Ratios
        if revenue != 0:
            ratios['current_assets_to_revenue'] = {
                'value': current_assets / revenue,
                'date': year_data['balance_sheet'].get('total_current_assets', {}).get('date')
            }
            
            ratios['current_liabilities_to_revenue'] = {
                'value': current_liabilities / revenue,
                'date': year_data['balance_sheet'].get('current_liabilities', {}).get('date')
            }
            
            ratios['net_fixed_assets_to_revenue'] = {
                'value': ppe_net / revenue,
                'date': year_data['balance_sheet'].get('ppe_net', {}).get('date')
            }
            
            ratios['operating_costs_to_revenue'] = {
                'value': cogs / revenue,
                'date': year_data['income_statement'].get('cost_of_goods_sold', {}).get('date')
            }
        
        # Calculate Interest Paid Rate on Cash and Securities
        if cash_and_securities != 0:
            ratios['interest_paid_rate'] = {
                'value': interest_paid / cash_and_securities,
                'date': year_data['income_statement'].get('interest_paid', {}).get('date')
            }
        
        # Get previous year values for averages
        if prev_year:
            prev_year_data = financial_data['years'][prev_year]
            prev_ppe_net = prev_year_data['balance_sheet'].get('ppe_net', {}).get('value', 0)
            prev_total_liabilities = prev_year_data['balance_sheet'].get('total_liabilities', {}).get('value', 0)
            
            # Calculate Depreciation Rate
            avg_ppe = calculate_average(ppe_net, prev_ppe_net)
            if avg_ppe and avg_ppe != 0:
                ratios['depreciation_rate'] = {
                    'value': depreciation / avg_ppe,
                    'date': year_data['income_statement'].get('depreciation', {}).get('date')
                }
            
            # Calculate Interest Rate
            avg_liabilities = calculate_average(total_liabilities, prev_total_liabilities)
            if avg_liabilities and avg_liabilities != 0:
                ratios['interest_rate'] = {
                    'value': interest_paid / avg_liabilities,
                    'date': year_data['income_statement'].get('interest_paid', {}).get('date')
                }
        
        # Calculate Tax Rate
        if profit_before_tax != 0:
            tax_rate = (profit_before_tax - profit_after_tax) / profit_before_tax
            ratios['tax_rate'] = {
                'value': tax_rate,
                'date': year_data['income_statement'].get('profit_before_tax', {}).get('date')
            }
        
        # Calculate Dividend Growth Rate (only for the final year, idk if this should be hard coded,
        # I just saw it in Professor Wang's video. TODO: make this an option and not a requirment?
        if year == final_year:
            initial_dividend = financial_data['years'][first_year]['income_statement'].get('dividends', {}).get('value', 0)
            final_dividend = dividends
            num_years = len(years) - 1
            
            if initial_dividend != 0 and num_years > 0:
                growth_rate = (pow(final_dividend / initial_dividend, 1/num_years) - 1)
                ratios['dividend_growth_rate'] = {
                    'value': growth_rate,
                    'date': year_data['income_statement'].get('dividends', {}).get('date')
                }
    
    return results