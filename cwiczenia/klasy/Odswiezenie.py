users = {'Jasio': 'aktywny', 'Pawel': 'nieaktywny', 'Patiszon': 'aktywny'}
druga_lista = ['pawel', 'i', 'gawel', 'w', 'jednym', 'spali', 'domku']

for user, statusUsera in users.items():
    if statusUsera == 'nieaktywny':
        print(user)

for dlugoscSlowa in range(len(druga_lista)):
    print(dlugoscSlowa, druga_lista[dlugoscSlowa])