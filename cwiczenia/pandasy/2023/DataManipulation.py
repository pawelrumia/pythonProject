import pandas as pd
import numpy as np
import datetime as dt

data = np.genfromtxt('data/example_data.csv', delimiter=';',
                     names=True,dtype=None,encoding='UTF')

# print(data.dtype)

array_dict = {
    col: np.array([row[i] for row in data])
    for i, col in enumerate(data.dtype.names)
}
# print(array_dict)

seriesFromExampleData = pd.Series(array_dict['place'], name='Nazwa miejsca')
print(seriesFromExampleData)