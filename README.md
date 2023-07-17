# Time Series Forecasting

In this project, I tested various smoothing models (moving average, simple exponential, Holt's Linear, Holt-Winters) to determine which model best visualized and forecasted data. The models were evaluated by how well they smoothed out irregular roughness and how well they retained the trend and/or seasonality of the data. Using  machine learning, I analyzed data concerning the number of visits to a specific Udemy website over time.

**Packages Used**

- Openpyxl
- Pandas
- Numpy
- Statsmodels
- MatPlotLib
- Sklearn

**Results**

<img src="https://github.com/tanaysubramanian/time-series-forecasting/assets/139258609/9c1fe471-d305-4bb5-bd4d-4cfc3a9bd3fb" alt="Image" width="501.9" height="397.6"> <br />

<img src="https://github.com/tanaysubramanian/time-series-forecasting/assets/139258609/bf81a241-9139-4f83-bca8-899244709709" alt="Image" width="501.9" height="397.6"> <br />

<img src="https://github.com/tanaysubramanian/time-series-forecasting/assets/139258609/972cfce7-ae81-4187-a514-495681403d95" alt="Image" width="501.9" height="397.6"> <br />

NOTE: The simple exponential smoothing (above) and Holt-Linears (below) models did not clearly show the differences in curves in each of the 2 graphs when the full dataset was considered. Hence, both models were applied to the first part of the dataset to conveniently show the differences.

<img src="https://github.com/tanaysubramanian/time-series-forecasting/assets/139258609/3788f58a-3985-40f1-b8f2-6ccc98156142" alt="Image" width="501.9" height="397.6"> <br />

The below 2 graphs were produced by the Holt-Winters model.

<img src="https://github.com/tanaysubramanian/time-series-forecasting/assets/139258609/2c896be1-113a-4cd6-8a55-39c884b7eb99" alt="Image" width="550.2" height="299.6"> <br />

<img src="https://github.com/tanaysubramanian/time-series-forecasting/assets/139258609/662332fe-ec17-4cd3-9de6-ec76c83dc73a" alt="Image" width="501.9" height="397.6"> <br />

The Holt-Winters model seems to optimally smooth and forecast the data. This model best represents data with a trend and seasonality, whereas the simple exponential model is suited for data with no clear trend or seasonality, and the Holt-Liners model  is best for data with a trend but no seasonality.







