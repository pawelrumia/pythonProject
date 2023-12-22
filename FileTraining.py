# file = open('myNewFile.txt', 'x')
# data = 'Jakis tam tekst'
# file.write(data)
# file.close()

# reader = open('myNewFile.txt', 'r')
# data2 = reader.read()
# print(data2)
# reader.close()

data = [1.3, 2.4, 3.3, 4.1, 5.7]
f = open("myNewFile.txt", "x")

for value in data:
    record = str(value)
    f.write(record)
    f.write("\n")
f.close()
