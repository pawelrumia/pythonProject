import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

data = pd.read_csv("data/DailyDelhiClimateTrain.csv")
print(data.head())
print(data.describe())

result = px.line(data,
                 x='date',
                 y='meantemp',
                 title='Mean temp in Delphi')
result.show()

figure = px.scatter(data_frame=data, x="humidity",
                    y="meantemp", size="meantemp",
                    trendline="ols", trendline_scope="overall", trendline_color_override="black",
                    title="Relationship Between Temperature and Humidity")
figure.show()

data["date"] = pd.to_datetime(data["date"], format='%Y-%m-%d')
data['year'] = data['date'].dt.year
data["month"] = data["date"].dt.month
print(data.head())

print(plt.style.available)
plt.style.use('_mpl-gallery')
plt.figure(figsize=(15, 10))
plt.title('Temperatures')
sns.lineplot(data, x='month', y='meantemp', hue='year')
plt.show()

forecast_data = data.rename(columns = {"date": "ds",
                                       "meantemp": "y"})
print(forecast_data)

model = Prophet()
model.fit(forecast_data)
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
plot_plotly(model, forecast)


