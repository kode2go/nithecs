# -*- coding: utf-8 -*-
"""

@author: BBarsch

All code and lessons – github repo: 
    
    https://github.com/kode2go/nithecs
    
Discussions:
    
      https://github.com/kode2go/nithecs/discussions
      
Form:
    
    https://forms.office.com/r/2uE8yTrjhg

https://pandas.pydata.org/docs/user_guide/timeseries.html

https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-to-time-series-analysis/
https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/


"""
import pandas as pd
import matplotlib.pyplot as plt
import run_profile_report as rpp
import seaborn as sns


# Load the dataset
# Specify the index column, then you won't get unnamed: 0
df = pd.read_csv('weather.csv', parse_dates=['datetime'],index_col=0)

df.set_index('datetime', inplace=True)
df_split_date = df.copy()


ds = df_split_date.index.to_series()
df_split_date['month'] = ds.dt.month
df_split_date['day_of_week'] = ds.dt.dayofweek
df_split_date['day'] = ds.dt.day

# Set the Time column as the index
# df.set_index('datetime', inplace=True)

# df2 = pd.read_csv('weather.csv',header=0, infer_datetime_format=True, parse_dates=[0], index_col=[0])

'''Inspect the dataset to get a sense of its structure '''
rpp.generate_profile_report(df)


# # Print the first few rows
# print(df.head())

# # Check the data types and missing values
# print(df.info())

# # Get summary statistics
# print(df.describe())

# df2 = pd.read_csv('london_weather.csv' )
# print(df2.describe())

''' Visualize the data to identify trends, seasonality, and outliers '''

# Plot the TemperatureC and DewpointC columns
sns.lineplot(data=df[['count']])

# Set the title and axis labels
sns.set(rc={'figure.figsize':(11, 4)})
sns.set_style("whitegrid")
plt.title('Temperature and Precip over Time')
plt.xlabel('Time')
plt.ylabel('Degrees Celsius')

# Display the plot
plt.show()

'''Perform time series decomposition to separate the trend, seasonality, and residuals'''
from statsmodels.tsa.seasonal import seasonal_decompose

# Perform time series decomposition
decomposition = seasonal_decompose(df['count'], model='additive', period=12)

# Plot the decomposition
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(df['count'], label='Original')
plt.legend(loc='upper left')

plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='upper left')

plt.subplot(413)
plt.plot(seasonal, label='Seasonality')
plt.legend(loc='upper left')

plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

'''Check for autocorrelation and stationarity'''

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Plot autocorrelation function (ACF) and partial autocorrelation function (PACF)
fig, ax = plt.subplots(2, 1, figsize=(12,8))
plot_acf(df['temp'], lags=30, ax=ax[0])
plot_pacf(df['temp'], lags=30, ax=ax[1])
plt.show()


'''Perform time series forecasting using various models (e.g., ARIMA, SARIMA, Prophet, etc.)'''
from statsmodels.tsa.arima.model import ARIMA

# Fit an ARIMA model
# In this case, the order is set to (1,1,1), which means that the model has one autoregressive (AR) term, one differencing (I) term, and one moving average (MA) term.
model = ARIMA(df['temp'], order=(1,1,1))
model_fit = model.fit()

# Make predictions
# Finally, the predict() method is used to make future predictions for the next 12 time periods,
forecast = model_fit.predict(start=len(df), end=len(df)+11, typ='levels')

# Plot the forecast
plt.plot(df.index, df['temp'], label='Observed')
plt.plot(forecast.index, forecast.values, label='Forecast')
plt.legend()
plt.xticks(rotation='vertical')
plt.show()
