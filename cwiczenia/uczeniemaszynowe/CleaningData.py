import pandas as pd

data_frame = pd.read_csv('chapter3/nyc_temperatures.csv')
print(data_frame.columns)
print(data_frame.head())

data_frame.rename()