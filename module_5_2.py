class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Горький', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Простоквашино', 1)
h4 = House('ЖК Эльбрус', 30)
print(h1)
print(h2)
print(h3)
print(h4)
print(len(h1))
print(len(h2))
print(len(h3))
print(len(h4))
