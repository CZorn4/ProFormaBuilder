import requests
import pandas as pd

# Set pandas to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

headers = {'User-Agent': 'Sample Company Name AdminContact@company.com'}

# Get initial filing data
url = 'https://data.sec.gov/submissions/CIK0001045810.json'
r = requests.get(url, headers=headers)
data = r.json()

# Get recent filings
df_recent = pd.DataFrame(data['filings']['recent'])

# Get older filings from files
older_files = data['filings']['files']
if older_files:
    for file in older_files:
        file_url = f"https://data.sec.gov/submissions/{file['name']}"
        r = requests.get(file_url, headers=headers)
        file_data = r.json()
        df_older = pd.DataFrame(file_data)
        df_recent = pd.concat([df_recent, df_older], ignore_index=True)

# Drop the specified columns
columns_to_drop = ['size', 'isInlineXBRL', 'primaryDocument', 'primaryDocDescription']
df_recent = df_recent.drop(columns=columns_to_drop, errors='ignore')

# Filter for just 10-K and 10-Q
df_recent = df_recent[df_recent['form'].isin(['10-K', '10-Q'])]

print(f"Total number of 10-K and 10-Q filings: {len(df_recent)}")
print(df_recent)