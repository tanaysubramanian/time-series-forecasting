import openpyxl
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# preparing data
times = pd.read_csv("https://bit.ly/udemy_df", index_col = "Date", parse_dates = True) # index sets specific column as index instead of integers from 0. parse converts dates to hyphen instead of forward slash format
del times["Easter"] # removing extra columns
del times["Christmas"]
df = times.resample(rule = "MS").sum()  # new table with dates every month by summing all values in each month

# plotting seasonality and trend data
seasonal_decompose(df, model = "mul").plot()
plt.show()
df.shape # 60 rows

# train test split
train = df[:40]
test = df[40:]

# plotting holt winters
model = ExponentialSmoothing(train.Udemy, trend = "add", seasonal = "mul").fit()
test_pred = model.forecast(11)
test_pred

train["Udemy"].plot(legend = True, label = "Train", figsize = (9,6))
test["Udemy"].plot(legend = True, label = "Test", figsize = (9,6))
test_pred.plot(legend = True, label = "Predicted Test", figsize = (9,6))
plt.title("Holt-Winters")
plt.show()

# final model
final = ExponentialSmoothing(train.Udemy, trend = "add", seasonal = "mul").fit()
pred = final.forecast(10)
pred

df["Udemy"].plot(legend = True, label = "Udemy", figsize = (9,6))
pred.plot(legend = True, label = "Prediction", figsize = (9,6))
plt.title("Holt-Winters")
plt.show()
