def fibo(f):
    a, b = 0, 1
    while f > a:
        print(a, end=' ')
        a, b = b, a + b


def fibo_drugi_zapisz_na_liste(liczba):
    result = []
    a, b = 0, 1
    while a < liczba:
        result.append(a)
        print(a)
        a, b = b, a + b
    return result


def average(values):
    return sum(values) / len(values)


def multi_return(x, data):
    totalsum = 0
    for x in data:
        totalsum = totalsum + x

    N = len(data)
    mean = totalsum / N
    return totalsum, mean


def gadajaca_papuga(wiek, /, *, kolor='obrzyg', coMowi='krakra', typ='Norweska papuga'):
    print('To jest papuga zyjaca ', wiek, ' lat')
    print('papuga typu', typ)


def gadajacy_kotek(coMowiKotek, *args, **slowa):
    print('Kotek mowi: ', coMowiKotek)
    for a in args:
        print(a)
    for b in slowa:
        print(b, " : ", slowa[b])


my_table_of_contents = [1, 3, 2, 5, 7, 3]

print(average((1, 3, 4, 6)))

print(multi_return(4, my_table_of_contents))

print(fibo_drugi_zapisz_na_liste(250))

fibo(200)

gadajaca_papuga(30, typ='obrzygana')
gadajacy_kotek('Ja pierdole, jak mi sie nie chce', 'Co mowisz kotku', 'nie mow tak')
gadajaca_papuga(20, kolor='ryży', typ='ryży')
