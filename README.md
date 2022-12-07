# Python library about financial informations extraction tunisian companies in the stock market
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)   

## Functionality of pyfinance_tunisia

    Income statement indicators : EBIT ,EBITDA ,Gearing ,Return on equity ,Net profit...

    Balance sheet indicators : Net debt ,Need in funds ,Revenue ,Equity...

    Long term stock market indicator : P/E ,Dividend Yield ,P/B	,Pay out...	

    The company's shareholders : The shareholder name and the percentage % .

    Dividend : Dividend per share ,Distribution date ,Total amount...
## Usage

-Make sure you have Python installed in your system.

-Run Following command in the CMD.
 ```
  pip install pyfinance_tunisia .
  ```
## Example

 ```
from pyfinance_tunisia import list_stocks,company

#Fist you need to see all tunisian companies in stock market
Tunisian_stocks=list_stocks()

#Choose one company that we are intersting in .
# We take example of ADWYA company.

# With income_statement_indicators funtion  you can find the Return on equity ROE ratio,gearing ratio,EBIT and EBITDA and others for the last 4years
company('ADWYA').income_statement_indicators()

# With balance_sheet_indicators function you can find the most important ratios in the balancesheet for the last 4 years.
company('ADWYA').balance_sheet_indicators()

# stock_market_indicators function can help to find many stock market indicators like P/E ratio , Divended yield and P/B for the last 4 years.
company('ADWYA').stock_market_indicators()

# shareholders function is helpful to find list of shareholders in company that you are choosing .
company('ADWYA').shareholders()
  ```

