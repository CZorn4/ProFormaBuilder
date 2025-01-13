import requests
import time
import os
from dotenv import load_dotenv

# Load .env file from parent directory
load_dotenv()
user = os.environ.get('USER')

def make_http_request(url=None, cik=None,):
    """
    Make an HTTP request to the SEC API
    
    Args:
        url (str, optional): Full URL to request
        cik (str, optional): CIK number if requesting company data
        
    Returns:
        requests.Response or None: Response object if successful, None if failed
    """
    headers = {
        'User-Agent': {user}
    }
    
    if not url and not cik:
        raise ValueError("Either URL or CIK parameter is required")
    
    if url:
        request_url = url
    else:
        request_url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    
    try:
        # Add delay to respect SEC rate limits
        time.sleep(0.1)  # 100ms delay between requests
        
        response = requests.get(request_url, headers=headers)
        response.raise_for_status()
        return response
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None