import math

def formatowanie(kasa):
    print('Podaj imie:')
    imie = input()
    print(f'Hej {imie}, ty stary chuju; wisisz mi {kasa} dolcow')
    print(f'The value of pi is {math.pi:.5f}')

formatowanie(1562)

print('To jest testowy tekst {}'.format('w morde kopane'))
print('To jest testowy tekst {0}, {1}'.format('w morde kopane', 'niech to swisnie'))
print('To jest testowy tekst {bluzg}, {drugiBluzg}'.format(bluzg='w morde kopane', drugiBluzg='niech to swisnie'))

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
