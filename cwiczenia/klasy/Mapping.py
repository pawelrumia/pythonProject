class Mapping:
    def __init__(self, iterable):
        self.listItems = []
        self._update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.listItems.append(item)

    __update = update

class MappingSubclass(Mapping):
    def update(self, iterable, values):
        for item in zip(iterable, values):
            self.listItems.append(item)