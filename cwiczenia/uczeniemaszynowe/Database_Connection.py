import sqlite3

import pandas as pd

with sqlite3.connect('data/quakes.db') as connection:
    pd.read_csv('data/tsunamis.csv').to_sql(
        'tsunamis', connection, index=False,
        if_exists='replace')

with sqlite3.connect('data/quakes.db') as connection:
    tsunamisy = pd.read_sql('Select * from tsunamis where "mag" >= 6.6', connection)

print(tsunamisy)