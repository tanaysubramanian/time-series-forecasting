import openpyxl
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import Holt

# preparing data
times = pd.read_csv("https://bit.ly/udemy_df", index_col = "Date", parse_dates = True) # index sets specific column as index instead of integers from 0. parse converts dates to hyphen instead of forward slash format
del times["Easter"] # removing extra columns
del times["Christmas"]

# plotting original data
times.shape # yields total number of rows in table (1827)
plt.plot(times[1:100]["Udemy"]) # displays data in number of rows within range of index
plt.xticks(rotation = 30) # rotation is number of degrees which x axis ticks are rotated for better visibility

# plotting holt smoothing
data = times[1:100]
fit1 = Holt(data).fit()
fit2 = Holt(data, exponential = True).fit()

plt.figure(figsize = (9,6))
plt.plot(times[1:100], label = "Original Data", color = "black")
plt.xticks(rotation = 30)
#plt.plot(pd.date_range(start="2020-12-01", periods=6, freq="M"), forecast, label="Forecast")
plt.plot(fit1.fittedvalues, label = "Linear Trend", color = "blue")
plt.plot(fit2.fittedvalues, label = "Exponential Trend", color = "red")
plt.title("Holt's Linear")
plt.legend()
plt.show()