import pandas as pd
import numpy as np
import datetime as dt

dates = pd.date_range('20231103', periods = 5, freq='M')
print(dates)
series = pd.Series([1,2,3,4,5], index=dates)
print(series)

days = series.describe()
print(days)