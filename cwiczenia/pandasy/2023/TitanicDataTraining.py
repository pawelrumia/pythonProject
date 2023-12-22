import pandas as pd

titanic = pd.read_csv("data/titanic.csv")
print(titanic.head())

names = titanic["Name"]
print(names.head(15))

ile_przezylo = titanic.loc[titanic["Survived"] == 1]
print(ile_przezylo.count())
