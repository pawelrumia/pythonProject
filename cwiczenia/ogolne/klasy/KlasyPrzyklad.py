class KlasyPrzyklad:

    def __init__(self, imie):
        self.imie = imie
        self.triki = []

    def addTrick(self, trik):
        self.triki.append(trik)

a = KlasyPrzyklad("Plugger")
b = KlasyPrzyklad("Wtyczek")
a.addTrick("uciekaj")
b.addTrick("kradnij zarcie")

print(a.triki)
print(b.triki)