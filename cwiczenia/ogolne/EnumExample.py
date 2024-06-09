from enum import Enum
class Color(Enum):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'

color = Color(input('Podaj kolor:'))

match color:
    case Color.RED:
        print('Red is bad')
    case Color.GREEN:
        print('Green is badder')
    case Color.BLUE:
        print('Niebieski is the baddest')
    case _:
        raise ValueError('nie ma takego koloru!')