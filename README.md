# Pro Forma Builder

A Python-based tool for building pro forma financial statements by fetching and analyzing data from the SEC's CompanyFacts API endpoint. This tool automatically retrieves historical financial data and prepares it for financial analysis and forecasting.

## Features

- Fetches financial data directly from SEC EDGAR database
- Supports both basic (annual) and detailed (including quarterly) financial statements
- Handles XBRL-tagged data for accurate financial line item mapping
- Debug mode for detailed process logging
- Optional data export to Excel
- Configurable projection periods

## Notes about SEC API strategy
There is no true universal way that every company uses to file their financial reports. the SEC uses XBRL 
(eXtensible Business Reporting Language) as a general guideline for filing fincancials, but one company might use
a tag set that another doesnt. I have designed a way to aggregate line items into financial periods based on matching the
report dates from the company "submissions" endpoint to the report dates for the raw line item in the "companyfacts" endpoint.
you can run the two tests in the tests folder to see how the raw data looks, . I chose this way because I tried a bunch of other ways
and this way produced the least amount of edge cases. It is important to understand that you cannot rely on one system to work the same for every comapny, because pretty much every rule ever created by the SEC has some sort of work around. I have no clue if this way is remotely the best way, but it works for now.

companyfacts endpoint -

sometimes companys will make reversions of something that causes the line items report to not be in the order you expected it to be.
The only universal attributes you can rely on are an end date, and the name of the tag. if it isnt a balance sheet item, it will have a start date too. however, the company can report something like a "9 months ended" along with a "3 months ended" on one 10-Q. this means that the system has to properly pick up the correct tag. you cant base the entire system on this though because like I said, balance sheet items obvously just carry a balance, and its not a period report item. the system that I have (so far) found to work best goes like this:

1. if there is only one item with the matching end date, record that item and move on.

2. if there are multiple, first filter for ones with a non-null frame value.

3. if there are multiple with frames, get the latest entry

4. if none of them have frames (but there are multimple without), also just get the latest entry

So far, I havent had many issues with this. The only issue is when an item is filed in a way that no other is filed for, like some items only have Q3 reports for some random reason. this will still match the end date proprely and reord the item, but you will see that the start date is different than any other item in the period, meaning that the analysis engine will have to be built to take start dates into account to resolve this case. Here is an example, Apple's "deferred income tax" is reported in 3 quarter intervals and never in 1 quarter intervals. the only way around this would be to just drop the item but I am not going to do that.

```
Income Before Tax:
Income Before Tax                             $2,784,000,000.00 (2024-07-01 to 2024-09-30)

Income Taxes:
Current Income Tax                            No data
Deferred Income Tax Expense Benefit           $418,000,000.00 (2024-01-01 to 2024-09-30) <-------
Income Tax Expense                            $601,000,000.00 (2024-07-01 to 2024-09-30)
Provision For Income Taxes                    No data

Net Income:
Profit Loss                                   $2,183,000,000.00 (2024-07-01 to 2024-09-30)
Income From Noncontrolling Interests          $16,000,000.00 (2024-07-01 to 2024-09-30)
Net Income                                    $2,167,000,000.00 (2024-07-01 to 2024-09-30)
```
submissions endpoint - 

this one is way more simple. just query the endpoint, sort for items where the form is 10-K or 10-Q and the "isXBRL" is "1",
and record items. if the user set the system to basic, just return the 10-K's and if its detailed, return both. note that the report date (synonymous to end date) is the most important piece of information to return here, because as I said before, its the most reliable piece of data in the database. If you have the report date, you can jsut match the end date of the line items to effectivley "reconstruct" the
most universal form of the financial report at that date.


## Installation

Clone the repository:
```
git clone [your-repo-url]
cd pro-forma-builder
```

Install dependencies:
```
pip install -r requirements.txt
```

## Usage
Firstly, make an .env file and include the User-Agent header that will be sent to the SEC endpoints. They require an email. I would structure it like this:

```
USER = "Your Name youremail@email.com"
```

The tool can be run from the command line with various options:

```
python main.py TICKER [--basic YEARS | --detailed YEARS] [options]
```

### Required Arguments
- `TICKER`: Stock ticker symbol (e.g., AAPL, MSFT)
- One of the following modes:
  - `--basic YEARS`: Fetch only annual reports for specified number of years
  - `--detailed YEARS`: Fetch both annual and quarterly reports for specified number of years

### Optional Arguments
- `--debug`: Enable debug mode with additional output
- `--print`: Print formatted financial statements to console

### Examples

Basic usage with annual data:
```
python main.py AAPL --basic 3
```

Detailed data with debug output:
```
python main.py MSFT --detailed 5 --debug
```


## Project Status

Currently in active development. Working on implementing:
- Future cash flow modeling and projections based on historical data
- Enhanced forecasting algorithms
- Additional financial metrics and ratios
- Improved data visualization options

## Future Plans

- Implement machine learning models for more accurate projections
- Add support for competitor analysis
- Integrate industry-specific metrics
- Build a web interface for easier data visualization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

collin.zorn@gmail.com
