# Getting the data

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

yf.pdr_override()

tickers = ['IWM', '^GSPC', 'QQQ', 'AAPL']
startdate = '2020-01-01'
enddate = '2021-03-08'

data = pdr.get_data_yahoo(tickers, start=startdate, end=enddate)['Adj Close']

# Variables

num_assets = len(tickers)
weights = np.random.random(num_assets)
weights /= np.sum(weights)
returns = data.pct_change()   # Daily Returns

# Cummulative Returns

cummulative_returns = (1+returns).cumprod()
cummulative_returns.fillna(1, inplace=True)

# Compound Annual Growth Rate (CAGR)

cagr = cummulative_returns**(252/len(cummulative_returns))-1

# Portfolio CAGR

portfolio_cagr = np.dot(cagr.iloc[-1:], weights)

# Equal Weight (EW)

weights_1 = np.array([0.25, 0.25, 0.25, 0.25])

returns['EW'] = returns.dot(weights_1)
cummulative_returns_1 = (1+returns).cumprod()
cummulative_returns_1.fillna(1, inplace=True)
portfolio_cummulative_returns = cummulative_returns_1['EW']

# Drawdown (DD)

maxr = portfolio_cummulative_returns.cummax()
drawdown = (portfolio_cummulative_returns - maxr) / maxr

ddmax = drawdown.min()