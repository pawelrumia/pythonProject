import matplotlib.pyplot as plt
import pandas as pd

wide_df = pd.read_csv("wide_data.csv", parse_dates=['date'])

long_df = pd.read_csv(
    'long_data.csv',
    usecols=['date', 'datatype', 'value'],
    parse_dates=['date']
)[['date', 'datatype', 'value']] # sort columns

print(wide_df.describe(include='all', datetime_is_numeric=True))

print(wide_df)
wide_df.plot(
    x='date', y=['TMAX', 'TMIN', 'TOBS'], figsize=(15, 5),
    title='Temperatura w NYC'
    ).set_ylabel('Temperatura w Celsjuszach')
plt.show()