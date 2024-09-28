class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self


h1 = House('ЖК Горький', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Простоквашино', 1)
h4 = House('ЖК Эльбрус', 30)
print(h1)
print(h2)
print(h3)
print(h4)
print(f'{h1.number_of_floors} равно {h2.number_of_floors}:', h1 == h2)  # __eq__
h1 = h1 + 12  # __add__
print(h1)
print(f'{h1.number_of_floors} равно {h4.number_of_floors}:', h1 == h4)
print(f'{h2.number_of_floors} равно {h3.number_of_floors}:', h2 == h3)
h2 = 7 + h2  # __radd__
print(h2)
h3 += 8  # __iadd__
print(h3)
print(f'{h2.number_of_floors} равно {h3.number_of_floors}:', h2 == h3)
print(f'{h1.number_of_floors} > {h2.number_of_floors}:', h1 > h2)  # __gt__
print(f'{h1.number_of_floors} >= {h2.number_of_floors}:', h1 >= h2)  # __ge__
print(f'{h1.number_of_floors} < {h2.number_of_floors}:', h1 < h2)  # __lt__
print(f'{h1.number_of_floors} <= {h2.number_of_floors}:', h1 <= h2)  # __le__
print(f'{h1.number_of_floors} != {h2.number_of_floors}:', h1 != h2)  # __ne__
