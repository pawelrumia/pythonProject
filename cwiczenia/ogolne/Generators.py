import random

print(sum(i + i for i in range(1, 10)))

lista = [1,2,3,4]

data = 'Pati'
imie = 'Patison'
print(list(data[i] for i in range(len(data) - 1, -1, -1)))

a = random.randint(0, 10)
if (a <= 5):
   print(f"losowy number generated below or equal 5, number: ${a}")
else:
    print(f"Your are lucky, punk, a=${a}")


print(data[2])
print("Zonka : %s" %imie)

for x in lista:
    print("wartosc x: {}".format(x))