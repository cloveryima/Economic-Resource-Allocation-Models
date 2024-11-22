import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data/sample_demand.csv')  # Replace with your actual file
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Time Series Forecasting with Holt-Winters
def holt_winters_forecast(data, forecast_periods):
    model = ExponentialSmoothing(data['Demand'], trend='add', seasonal='add', seasonal_periods=12)
    hw_model = model.fit()
    forecast = hw_model.forecast(steps=forecast_periods)
    return forecast

# Machine Learning for Demand Forecasting
def random_forest_forecast(data):
    X = data[['Feature1', 'Feature2']]  # Replace with relevant features
    y = data['Demand']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("RMSE:", np.sqrt(mean_squared_error(y_test, predictions)))
    return predictions

# Visualize Results
forecast_periods = 12
forecast = holt_winters_forecast(data, forecast_periods)
data['Demand'].plot(label='Actual', legend=True)
forecast.plot(label='Forecast', legend=True)
plt.title("Demand Forecasting")
plt.show()
