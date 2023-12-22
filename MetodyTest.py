import math

rok = 2015
imie = 'Patrycja'

for i in reversed(range(1, 10, 2)):
    print(i)

liczby = [54, 34.2, float('NaN'), 33.2, 67.2, float('NaN'), 55.1]
filtered = []
for value in liczby:
    if not math.isnan(value):
        filtered.append(value)

print(filtered)
print(f'Byl rok {rok} a ona na imie miala {imie}')

liczba_wypitego = 1567
liczba_wszystkiego = 2888
procent = liczba_wypitego / (liczba_wszystkiego + liczba_wypitego)
print(' liczba_wypitego daje {:2.3%}'.format(liczba_wypitego, procent))
