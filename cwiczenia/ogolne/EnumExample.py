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
        print('Green jest dla świn')
    case Color.BLUE:
        print('Niebieski kureki')
    case _:
        raise ValueError('nie ma takego koloru!')