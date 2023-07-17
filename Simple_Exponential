import openpyxl
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing

# preparing data
times = pd.read_csv("https://bit.ly/udemy_df", index_col = "Date", parse_dates = True)
del times["Easter"]
del times["Christmas"]

# plotting original data
times.shape
plt.plot(times[1:100]["Udemy"])
plt.xticks(rotation = 30)

# plotting simple exponential smoothing and forecasting
data = times[1:100]
fit1 = SimpleExpSmoothing(data).fit(smoothing_level = 0.2, optimized = False)
fit2 = SimpleExpSmoothing(data).fit(smoothing_level = 0.8, optimized = False)
#forecast = SimpleExpSmoothing(data).fit().forecast(steps=6)

plt.figure(figsize = (9,6))
plt.plot(times[1:100], label = "Original Data", color = "black")
plt.xticks(rotation = 30)
plt.plot(fit1.fittedvalues, label = "Less Recency Weight", color = "blue")
plt.plot(fit2.fittedvalues, label = "More Recency Weight", color = "red")
plt.title("Simple Exponential Smoothing")
plt.legend()
plt.show()
