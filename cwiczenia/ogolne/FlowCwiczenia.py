a = 5
b = 8

if a > b:
    print("a jest wieksze niz b")
else:
    print("nie jest wieksze")


arrajka = [1.2, 3.1, 2.8, 4.4]
size = len(arrajka)
print(f'size arrajki = {size}')

for x in arrajka:
    print(x)

arrajka.append(4.7)
arrajka[3] = 11.1
for x in arrajka:
    print(x)
