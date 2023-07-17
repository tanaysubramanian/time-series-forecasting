import openpyxl
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# preparing data
times = pd.read_csv("https://bit.ly/udemy_df", index_col = "Date", parse_dates = True) # index sets specific column as index instead of integers from 0. parse converts dates to hyphen instead of forward slash format
del times["Easter"] # removing extra columns
del times["Christmas"]

# plotting original data
times.shape # yields total number of rows in table (1827)
plt.plot(times[1:1800]["Udemy"]) # displays data in number of rows within range of index
plt.xticks(rotation = 30) # rotation is number of degrees which x axis ticks are rotated for better visibility
plt.title("Original Dataset")

# plotting moving/rolling average
rollingseries = times[1:1800].rolling(window = 50) # rolling average smoothing reduces noise by taking snapshot mean of data over window of every 60 rows
rollingmean = rollingseries.mean()
rollingmean.plot(color = "red")
plt.title("Moving Average")
plt.show()