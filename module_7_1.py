from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        if isinstance(name, str):
            self.name = name
        if isinstance(weight, float):
            self.weight = weight
        if isinstance(category, str):
            self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        string = ''
        file = open(self.__file_name, 'r')
        for line in file:
            string += line
        file.close()
        return string

    def add(self, *products):
        for i in products:
            string = self.get_products()
            if i.name not in string:  # Ищем по наименованию продукта!
                # if str(i) not in string: # Ищем как в примере к заданию по всей строке!
                file = open(self.__file_name, 'a')
                file.write(str(i) + '\n')
                file.close()
            else:
                # print(f'Продукт {i} уже есть в магазине') # print как в примере к заданию
                print(f'Продукт {i.name} уже есть в магазине')  # print по заданию


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
