users = {'Jasko' : 'active', 'Patiszon': 'active', 'dziad': 'nieaktywny', 'Pawel': 'active', 'zbych': 'nieaktywny'}

aktywneJuzery = {}
for user, status in users.copy().items():
    print('przed petla:', users)
    if status == 'nieaktywny':
        print('wypierdalam:', users[user])
        del users[user]
        print('w petli:', users)
    elif status == 'active':
        aktywneJuzery[user] = status

print(users)
print('aktywne:', aktywneJuzery)

for x in range(1, 50):
    if x % 2 ==0:
        print("parzysty!", x)
        continue
    else:
        print("nieparzysty!:", x)
