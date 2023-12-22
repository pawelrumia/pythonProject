a = 5
print(type(a))
liczbyRozne = [-1, 2, 5, 7, -3, 0, 9, -2, -4]
wynik = [x for x in liczbyRozne if x >= 0]
print('To jest wynik', wynik)

listaNiezla = [(x, x+2, x+3) for x in liczbyRozne]
liczbyAbsolutne = [abs(x) for x in liczbyRozne]
print(liczbyAbsolutne)
print(listaNiezla)

mojSet = {'lecimy', 'pati', 'pati', 'jasio'}
print(mojSet)

mojDict = dict({1:'Pati', 2:'Pawel'})
print(mojDict)

squares = []
for i in range(0,7):
    squares.append(i ** 2)

print(squares)