# Portfolio Analysis

This code provides an analysis of a portfolio consisting of four assets: IWM, ^GSPC, QQQ, and AAPL. The data for the assets is retrieved from Yahoo Finance using the yfinance and pandas_datareader libraries.

## Requirements

The code requires the following Python libraries to be installed:

- pandas
- numpy
- yfinance
- matplotlib
- pandas_datareader

You can install the libraries using pip and the provided requirements.txt file.

```

pip install -r requirements.txt

```

## Data Retrieval

The data for the assets is retrieved using pandas_datareader and the Yahoo Finance API. The data retrieved is the adjusted close price for the assets from January 1, 2020, to March 8, 2021.

## Variables

The code calculates the daily returns for the assets and defines the number of assets and weights for the portfolio. The weights are randomly generated and normalized to ensure that they sum up to 1.

## Portfolio Metrics

The code calculates the following metrics for the portfolio:

- Cumulative Returns
- Compound Annual Growth Rate (CAGR)
- Equal Weighted Returns (EW)
- Drawdown (DD)

The cumulative returns are calculated from the daily returns using the cumprod() function. The CAGR is calculated using the cumulative returns and assuming 252 trading days in a year. The EW returns are calculated using an equal-weighted approach. The drawdown is calculated as the percentage decline in portfolio value from its historical peak.

## Conclusion

This code provides a basic analysis of a portfolio consisting of four assets. It can be modified to include additional assets or to adjust the portfolio weights.
