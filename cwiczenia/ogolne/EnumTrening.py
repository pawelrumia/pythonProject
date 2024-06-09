from enum import Enum

class Colory(Enum):
    RED = 'red'
    BLUE = 'blue'
    WHITE = 'white'

def maczowanieKolorow():
    color = Colory(input('Podaj swoj kolor: '))
    match color:
        case Colory.RED:
            print('Red kolor')
        case Colory.BLUE:
            print('Blue kolor')
        case Colory.WHITE:
            print('White kolor')

def ask_ok(prompt, retries = 4, reminder = "Jeszcze raz"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# maczowanieKolorow()

ask_ok('Enter your value', 2)