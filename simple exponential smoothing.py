# time series forecasting method which assigns higher weights to recent data and exponentially decreasing weights to older data
# useful for smoothing out fluctuations and determining trends from time series data
# 3 kinds smoothing: 
    # Simple/Exponential: no clear trend or seasonality in data (1 parameter: alpha for level smoothing) and assumes constant forecasting level
    # Holt's Linear: linear trend but no seasonality in data (2 parameters: alpha, beta for trend smoothing)
    # Holt-Winters: trend and seasonality in data (3 parameter: alpha, beta, gamma for seasonal smoothing)

import openpyxl
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing

# preparing data
times = pd.read_csv("https://bit.ly/udemy_df", index_col = "Date", parse_dates = True) # index sets specific column as index instead of integers from 0. parse converts dates to hyphen instead of forward slash format
del times["Easter"] # removing extra columns
del times["Christmas"]

# plotting original data
times.shape # yields total number of rows in table (1827)
plt.plot(times[1:100]["Udemy"]) # displays data in number of rows within range of index
plt.xticks(rotation = 30) # rotation is number of degrees which x axis ticks are rotated for better visibility

# plotting simple exponential smoothing and forecasting
data = times[1:100]
fit1 = SimpleExpSmoothing(data).fit(smoothing_level = 0.2, optimized = False) # greater smoothing level assigns more weight to more recent data
fit2 = SimpleExpSmoothing(data).fit(smoothing_level = 0.8, optimized = False)
#forecast = SimpleExpSmoothing(data).fit().forecast(steps=6) # greater steps forecasts more into the future

plt.figure(figsize = (9,6))
plt.plot(times[1:100], label = "Original Data", color = "black")
plt.xticks(rotation = 30)
plt.plot(fit1.fittedvalues, label = "Less Recency Weight", color = "blue")
plt.plot(fit2.fittedvalues, label = "More Recency Weight", color = "red")
plt.title("Simple Exponential Smoothing")
plt.legend()
plt.show()