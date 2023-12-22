from cwiczenia.klasy.KlasyPrzyklad import KlasyPrzyklad


class KlasaKtoraDziedziczy(KlasyPrzyklad):
    liczba = 0
    def __init__(self, liczba):
        self.liczba = liczba


x = KlasaKtoraDziedziczy(15)
print(x.liczba)
print(x.addTrick('podaj kase'))
print(x.triki)