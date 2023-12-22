import pandas as pd

data = {'Name': ['Pawel', 'Patrycja', 'Jasio'], 'Wiek': [37, 36, 5]}

df = pd.DataFrame(data)
print(df.head())
disctonary = [{'Name': 'Pawel', 'wiek': 36}, {'Name': 'Patrycja', 'wiek': 35}, {'Name': 'Jasio', 'wiek': 6}]
df2 = pd.DataFrame(disctonary)
print(df2.head())
print(df2)

tuples = [('Jasio', 24), ('Stasio', 25), ('Grzesio', 30)]
df3 = pd.DataFrame(tuples)
print(df3)

prawdziwyDataFrame = pd.read_csv("WHO_first9cols.csv")
print(prawdziwyDataFrame.head())
series_country = prawdziwyDataFrame['Country']
print("Kantry:", series_country)
print("Shape:", prawdziwyDataFrame.shape)
print("Columns;", prawdziwyDataFrame.columns)
print(series_country[-5:])
print(prawdziwyDataFrame.describe())
print(prawdziwyDataFrame.count())
continent = prawdziwyDataFrame.groupby('Continent').mean()
print(continent)
plodnosc = prawdziwyDataFrame.groupby('Continent').mean()['Adolescent fertility rate (%)']
print("Plodnosc:", plodnosc)

