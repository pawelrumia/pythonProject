class Osprzet:
    def __init__(self, model, color, weight=100, damaged=False):
        self.model = model
        self.color = color
        self.weight = weight
        self.damaged = damaged

    def display_car(self):
        print(f'Color of the car is {self.color} and model is {self.model}')

    def is_damaged(self):
        return self.damaged


car = Osprzet('Kijanka', 'White', 2345, True)
car.display_car()
print(car.is_damaged())
