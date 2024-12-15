import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_risk_free_rate():

    try:
        # pull risk-free rate directly
        treasury = yf.Ticker("^IRX")
        current_rate = treasury.info['regularMarketPrice'] / 100  # Convert basis points to decimal
        return current_rate
    except:
        return 0.05  # Fallback to 5% if unable to fetch

def calculate_beta(ticker, years=10):

    end_date = datetime.now()
    start_date = end_date - timedelta(days=years*365)
    
    # Get stock and market data
    stock = yf.Ticker(ticker)
    market = yf.Ticker('^GSPC')
    
    # Get monthly data
    stock_data = stock.history(start=start_date, end=end_date, interval='1mo')
    market_data = market.history(start=start_date, end=end_date, interval='1mo')
    
    # Calculate monthly returns
    stock_returns = stock_data['Close'].pct_change().dropna()
    market_returns = market_data['Close'].pct_change().dropna()
    
    # Combine into DataFrame and remove any rows with missing data
    returns_df = pd.DataFrame({
        'stock_returns': stock_returns,
        'market_returns': market_returns
    }).dropna()
    
    # Calculate beta using covariance method
    covariance = returns_df.cov().iloc[0,1]
    market_variance = returns_df['market_returns'].var()
    beta = covariance / market_variance
    
    # Calculate R-squared
    correlation = returns_df.corr().iloc[0,1]
    r_squared = correlation ** 2
    
    return beta, r_squared

def get_normalized_tax_rate(ratio_data):

    tax_rate_sum = 0
    tax_rate_count = 0
    
    for year in sorted(ratio_data['years'].keys()):
        if 'tax_rate' in ratio_data['years'][year]['ratios']:
            tax_rate = ratio_data['years'][year]['ratios']['tax_rate']['value']
            tax_rate_sum += tax_rate
            tax_rate_count += 1
    
    if tax_rate_count > 0:
        return tax_rate_sum / tax_rate_count
    return 0.21  # Fallback to standard corporate tax rate

def calculate_wacc(ticker, financial_data, ratio_data, market_risk_premium=0.06):

    # Calculate beta
    beta, r_squared = calculate_beta(ticker)
    
    # Get current risk-free rate
    risk_free_rate = get_risk_free_rate()
    
    # Get latest year's data
    latest_year = max(financial_data['years'].keys())
    latest_data = financial_data['years'][latest_year]
    latest_ratios = ratio_data['years'][latest_year]['ratios']
    
    # Get cost of debt from our ratio calculations
    cost_of_debt = latest_ratios['interest_rate']['value']
    
    # Get normalized tax rate
    tax_rate = get_normalized_tax_rate(ratio_data)
    
    # Calculate cost of equity using CAPM
    cost_of_equity = risk_free_rate + beta * market_risk_premium
    
    # Calculate capital structure weights using book values
    total_debt = latest_data['balance_sheet']['total_liabilities']['value']
    equity = latest_data['balance_sheet']['StockHolders_Equity']['value']
    total_value = total_debt + equity
    
    debt_weight = total_debt / total_value
    equity_weight = equity / total_value
    
    # Calculate WACC
    wacc = (equity_weight * cost_of_equity + 
            debt_weight * cost_of_debt * (1 - tax_rate))
    
    return {
        'wacc': wacc,
        'cost_of_equity': cost_of_equity,
        'cost_of_debt': cost_of_debt,
        'beta': beta,
        'r_squared': r_squared,
        'risk_free_rate': risk_free_rate,
        'market_risk_premium': market_risk_premium,
        'debt_weight': debt_weight,
        'equity_weight': equity_weight,
        'tax_rate': tax_rate
    }