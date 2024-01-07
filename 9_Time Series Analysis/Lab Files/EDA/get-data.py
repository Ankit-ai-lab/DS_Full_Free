#Key Website: from https://www.alphavantage.co/ 
#Key Value: 6TVZOWHAW8FETQ5S

!pip install alpha_vantage

import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# set up the API key and other parameters
api_key = '6TVZOWHAW8FETQ5S'
ticker = 'TSLA'
start_date = '2021-01-01'
end_date = '2021-12-31'

# initialize the TimeSeries object with the API key
ts = TimeSeries(key=api_key, output_format='pandas')

# get the data and store it in a Pandas DataFrame
data, meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize='full')
df_tesla = data.loc[start_date:end_date]

# print the DataFrame
print(df_tesla)

