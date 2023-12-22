import pandas as pd
import numpy as np
import datetime as dt


array_dict = {
    column: np.array([row[x] for row in data])
    for x, column in enumerate(data.dtype.names)
}

earthquakes_df = pd.DataFrame(data)
print(earthquakes_df)
print(earthquakes_df.columns)
print(earthquakes_df.empty)
print(earthquakes_df.shape)
print(earthquakes_df.head())
print(earthquakes_df.dtypes)
print(earthquakes_df.describe())
print(earthquakes_df.describe(include=object))
print("------------------------------------------")
print(earthquakes_df.place.unique())
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(earthquakes_df.place.value_counts())
print("==============================================")
print(earthquakes_df.mag.var())
print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[")
print(earthquakes_df.mag)
print('dictionary:')
print(earthquakes_df[['mag', 'title']])
print('slicing:')
print(earthquakes_df[577:581])
print('chaining:')
print(earthquakes_df[['mag', 'sources']][100:104])
print("wieksze niz 7")
print(earthquakes_df[earthquakes_df.mag >= 7])
print("wieksze niz 7 oraz posortowane")
print(earthquakes_df.loc[
          earthquakes_df.mag >= 7, ['alert', 'mag', 'magType', 'title', 'tsunami', 'type']
      ])
print('kolejne filtrowanie:')
print(earthquakes_df.loc[
          (earthquakes_df.place.str.contains('Alaska')) & (earthquakes_df.alert.notnull()),
          ['alert', 'mag', 'magType', 'title', 'tsunami', 'type']
      ])
print('regular expressions:')
print(earthquakes_df.loc[
          (earthquakes_df.place.str.contains(r'CA|California$')) & (earthquakes_df.mag > 3),
          ['alert', 'mag', 'magType', 'title', 'tsunami', 'type']
      ])


