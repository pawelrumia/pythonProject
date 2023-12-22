import pandas as pd

series = pd.Series(['Pawel', 'Patrycja', 'Jasiulenka'])

print(series.values)
print(series)
print(series.get(2))
series[1] = "Zdzicho"
print(series)
series[5] = "Patryszka"
print(series)

for item in series:
    print(item)

secondSeries = pd.Series({'a': 'Jasiulenka', 'b': 'Patryszka', 'c': 'Mazurzysko'})
print(secondSeries)
print(secondSeries.get('b'))
print(secondSeries[2])
print(secondSeries.get('z', default=11))

print(secondSeries.describe())
print(secondSeries.describe().count())
print(secondSeries.all())

is_in = 'Dynks' in secondSeries
print(is_in)
