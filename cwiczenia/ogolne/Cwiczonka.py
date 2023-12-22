i = 5
def f(arg = i):
    print(arg)

i = 6
f()
print("--------------------------------------")
def papuga(voltage, chuj='chuj', akcja='kop w dupe',typ='niejadalny'):
    print("Ta papuga typu", typ,"nie bedzie leciala, jesli sie ja jebnie z", voltage, "woltow")
    print("Ewentualnie trzeba zrobic akcje", akcja, "a jak to nie zadziala to", chuj)

papuga(1000)
papuga(2000, chuj='niech spierdala')
papuga(3000, chuj='zaraz jej wpierdole', akcja='podtopienie')