import pandas as pd

df = pd.read_csv('data/earthquakes.csv',
                 usecols=['time', 'title', 'place', 'magType', 'mag', 'alert', 'tsunami'])

print(df)
df['zrodlo'] = 'Mazur'
print(df)
print(df.place.unique)

print(df.assign(
    in_puerto = df.place.str.endswith('Puerto Rico'),
    in_ca = df.place.str.endswith('CA'),
    neither = lambda x: ~x.in_puerto & ~x.in_ca
).sample(5, random_state=0))

df_withTsunami = df[df.tsunami == 1]
df_noTsunami = df[df.tsunami == 0]

print(df_withTsunami.loc[
          (df_withTsunami.place.str.contains(r'CA|California$')),
          ['alert', 'mag', 'magType', 'title', 'tsunami']
      ])

print(df_noTsunami.loc[
          ((df_noTsunami.place.str.contains(r'CA|California$')) & (df_noTsunami.mag > 3)),
          ['alert', 'mag', 'magType', 'title', 'tsunami']
      ])