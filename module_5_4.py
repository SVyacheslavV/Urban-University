class House:
    houses_history = []

    def __new__(cls, *args):
        House.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Горький', 18)
print(House.houses_history)
h2 = House('Домик в деревне', 2)
print(House.houses_history)
h3 = House('Простоквашино', 1)
print(House.houses_history)
h4 = House('ЖК Эльбрус', 30)
print(House.houses_history)
del h1
del h2
print(House.houses_history)
