import openpyxl
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# preparing data
times = pd.read_csv("https://bit.ly/udemy_df", index_col = "Date", parse_dates = True)
del times["Easter"]
del times["Christmas"]

# plotting original data
times.shape
plt.plot(times[1:1800]["Udemy"])
plt.xticks(rotation = 30)
plt.title("Original Dataset")

# plotting moving/rolling average
rollingseries = times[1:1800].rolling(window = 50)
rollingmean = rollingseries.mean()
rollingmean.plot(color = "red")
plt.title("Moving Average")
plt.show()
