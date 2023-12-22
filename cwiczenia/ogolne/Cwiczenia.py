from datetime import date
import pandas as pd

now = date.today()
dataUr = date(1984, 9, 6)

ileJuzSieMecze = now - dataUr
print(ileJuzSieMecze.days)

s = 'Lecimy'
print(s[2:])

liczby = range(3, 12)
reversed = reversed(liczby)
reversed_lista = list(reversed)
print(reversed_lista)