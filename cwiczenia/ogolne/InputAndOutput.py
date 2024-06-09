import math

def formatowanie(kasa):
    print('Podaj imie:')
    imie = input()
    print(f'Hej {imie}, kolego ; wisisz mi {kasa} dolcow')
    print(f'The value of pi is {math.pi:.5f}')

formatowanie(1562)

print('To jest testowy tekst {}'.format('lelum polelum'))
print('To jest testowy tekst {0}, {1}'.format('lelum polelum', 'motyla noga'))
print('To jest testowy tekst {raz}, {dwa}'.format(raz='lelum polelum', dwa='motyla noga'))

def podzielnik(liczba, dzielnik):
    while liczba > 0:
        try:
            wynik = liczba / dzielnik
            print(wynik)
            break
        except ZeroDivisionError:
            print("nie dziel przez zeru")
            break

podzielnik(4, 3)
podzielnik(3, 0)
