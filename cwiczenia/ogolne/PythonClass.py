from cwiczenia.ogolne.PythonClassExtended import Osprzet


class Car(Osprzet):
    def __init__(self, model, color, silnik, szyberdach, weight=100, damaged=False):
        super().__init__(model, color, weight, damaged)
        self.silnik = silnik
        self.szyberdach = szyberdach

    def display_car(self):
        print(f'Silnik of the car is {self.silnik} and model is {self.model}')
        if self.model == 'meriwka':
            print('Złom!')

    def is_damaged(self):
        return self.damaged


auto = Car('meriwka', 'szary', 2.0, False, 1400, True)
car = Osprzet('Ibizka', 'yellow')
auto.display_car()
car.display_car()
print(auto.szyberdach)
