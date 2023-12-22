import pandas as pd
import numpy as np
import datetime as dt

data = np.genfromtxt('data/example_data.csv', delimiter=';',
                     names=True,dtype=None,encoding='UTF')

array_dict = {
    column: np.array([row[x] for row in data])
    for x, column in enumerate(data.dtype.names)
}

dataFrame = pd.DataFrame(array_dict)
print(dataFrame.get('place'))
print(dataFrame.dtypes)
print(dataFrame.columns)

pierwsza_kolumna = pd.Series(np.random.rand(5), name='Randomy')
print(pierwsza_kolumna)

my_dataFrame = pd.DataFrame(
    {
    'id': np.random.rand(5),
    'imie': ['pati', 'jasio', 'pawel', 'zdzich', 'rych'],
    'truth': [np.random.choice([True, False])
                for _ in range(5)]
    },
    index=pd.date_range(
        end=dt.date(2019, 4, 20),
        freq='1D', periods=5, name='date'
    )
)


print(my_dataFrame)