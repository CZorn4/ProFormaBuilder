import requests
import pandas as pd

pd.set_option('display.max_rows', None)

def fetch_company_facts(cik):
    cik = str(cik).zfill(10)
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 your.email@domain.com'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def analyze_revenue_tags(data):
    facts = data.get('facts', {}).get('us-gaap', {})
    tag = 'DeferredIncomeTaxExpenseBenefit'
    
    if tag in facts:
        print(f"Available units for {tag}:")
        units = facts[tag].get('units', {})
        print(list(units.keys()))
        
        if units:  # If there are any units
            first_unit = list(units.keys())[0]  # Get the first unit
            entries = units[first_unit]
            df = pd.DataFrame(entries)
            df = df.sort_values('end')
            print(f"\nData using unit: {first_unit}")
            print(df)
        else:
            print("No units found")
    else:
        print(f"Tag {tag} not found in data")

def main():
    cik = "0001045810"  # NVDA
    data = fetch_company_facts(cik)
    analyze_revenue_tags(data)

if __name__ == "__main__":
    main()