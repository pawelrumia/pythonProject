import numpy as np
import pandas as pd

data = np.genfromtxt('data/example_data.csv', delimiter=';',
                     names=True,dtype=None,encoding='UTF')

print(data)
print(data.dtype)
# print(min([row[3] for row in data]))

array_dict = {
    column: np.array([row[x] for row in data])
    for x, column in enumerate(data.dtype.names)
}

# print(array_dict)
# print(array_dict['mag'].max())
# print(array_dict['time'])

arraj_mag = array_dict['mag']
arraj_mag_series = pd.Series(array_dict['mag'])
print(arraj_mag_series.index)
print(array_dict['alert'])
print(arraj_mag_series)

# print(np.array([
#         value[array_dict['mag'].argmax()]
#         for key, value in array_dict.items()
#     ]))
x = pd.Series(arraj_mag)
print(x)