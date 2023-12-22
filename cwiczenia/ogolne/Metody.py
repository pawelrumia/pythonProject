users = {"Pawel": "super", "Patrycja": "super", "Putin": "bydlak"}
lista = [3, 4, 6, 2, 7, 4, 7, 4, 2]


def petlaFor():
    for name, stan in users.items():
        if stan == "bydlak":
            print("O to bydlak " + name)

def petle():
    for a in range(2, 10):
        for b in range(2, a):
            if a % b == 0:
                print(a, 'equals', b, '*', a//b)
                break
            else:
                print(a, 'is a prime number')
                break


def iterowanie():
    for i in range(len(lista)):
        print(i, lista[i])


# petlaFor()

# iterowanie()
petle()

# print(sum(lista))
