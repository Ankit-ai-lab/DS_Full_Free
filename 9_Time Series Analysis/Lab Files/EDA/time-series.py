#Install Pandas Data Reader
pip install pandas-datareader

#If not working try using the following command for Installing Pandas Data Reader
pip install --user pandas-datareader


#Import Pandas Data Reader - Note required Python 3.10 or higher in my case
import pandas_datareader as pdr

#Import Pandas 
import pandas as pd

# To work with Time Series Data need 'datetime' library
from datetime import datetime

#Get Data from Pandas Data Reader

df_tesla = pdr.get_data_yahoo('TSLA') #keyword to get tesla share price data
#if not working directly try this
df_tesla = pdr.get_data_quandl('TSLA', api_key='zrbwAPcSE7PYyZVzVpFd')

#if not working, i tried this and it worked out
!pip install yfinance
import yfinance as yf
df2 = yf.download('RELIANCE', start='2021-01-01', end='2023-05-07')


type(df_tesla)   #to check data type
df_tesla.head()  #to check start date of data
df_tesla.tail() #to check end date of data

df_tesla.plot() 

df_tesla['High'].plot() #to plot high

df_tesla['Low'].plot() #to plot low

df_tesla['Low'].plot(figsize=(12,4))

#limit date of data

df_tesla['High'].plot(xlim = ['2020-01-01', '2022-01-01'], ylim = [0,900], figsize=(12,4))

#line style and coloring
df_tesla['High'].plot(xlim = ['2020-01-01', '2022-01-01'], ls = '--', c ='green',ylim = [0,900], figsize=(12,4))

