import requests

def get_cik_from_ticker(ticker):
    
    # SEC-maintained JSON file for mapping tickers to CIKs
    url = "https://www.sec.gov/files/company_tickers.json"

    # SEC requires User-Agent header or you will recieve 403. DEV NOTE: CHANGE FROM YOUR NAME IF THIS CODE MAKES PROD
    headers = {
        "User-Agent": "OU Research Project (email me at collin.d.zorn-1@ou.edu)"
    }

    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        company_data = response.json()
        
        # Search through companies for matching ticker
        ticker = ticker.upper()
        for company in company_data.values():
            if company['ticker'] == ticker:
                if __name__ == "__main__":
                    return str(company['cik_str']).zfill(10), company['title']
                else:
                # Pad CIK with leading zeros to make it 10 digits
                    return str(company['cik_str']).zfill(10)
            
                
        raise ValueError(f"Could not find CIK for ticker {ticker}")
        
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch ticker data: {e}")


if __name__ == "__main__":
    ticker = "TSLA" # NOTE: forgetting that NVDA is set here leads to the misconception that you are not using NVDA
    cik, company_name = get_cik_from_ticker(ticker)
    print(f"Your CIK for {ticker} ({company_name}) is {cik}")