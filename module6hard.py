import math


class Figure:
    side_count = 0

    def __init__(self, color, *side):
        self.__sides = self.check_side(side)
        self.__color = list(color)
        self.filled = True

    def check_side(self, side):
        global side_count
        if len(side) == self.side_count:
            self.__sides = list(side)
        else:
            self.__sides = [1 for i in range(self.side_count)]
        return self.__sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        flag = True
        for i in color:
            if i < 0 or i > 255 or isinstance(i, float):
                flag = False
                break
        return flag

    def set_color(self, *color):
        if self.__is_valid_color(color) == True:
            self.__color = list(color)
            print('Изменился ', end='')
        else:
            print('Не изменился ', end='')

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, new_sides):
        if len(new_sides) != len(self.__sides):
            flag = False
            return flag
        if len(new_sides) == len(self.__sides):
            for i in new_sides:
                if not isinstance(i, int):
                    flag = False
                    break
                else:
                    flag = True
        return flag

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) == True:
            self.__sides = list(new_sides)
            print('Изменится ', end='')
        else:
            print('Не изменится ', end='')
        return self.__sides


class Circle(Figure):
    side_count = 1

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__radius = round(self.get_sides()[0] / (2 * math.pi), 2)

    def __len__(self):
        return self.get_sides()[0]

    def get_square(self):
        square = self.get_sides()[0] ** 2 / (4 * math.pi)
        return round(square, 2)


class Triangle(Figure):
    side_count = 3

    def __init__(self, color, *side):
        super().__init__(color, *side)

    def get_square(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        p = (a + b + c) / 2
        s_triangle = p * (p - a) * (p - b) * (p - c)
        return f'Площадь треугольника = {int(s_triangle)}'


class Cube(Figure):
    side_count = 12

    def __init__(self, color, *side):
        super().__init__(color, *side)

    def check_side(self, side):
        global side_count
        if len(side) == 1:
            self.__sides = list(side * self.side_count)
        else:
            self.__sides = [1 for i in range(self.side_count)]
        return self.__sides

    def __is_valid_sides(self, new_sides):
        if len(new_sides) != 1:
            flag = False
            return flag
        if len(new_sides) == 1:
            for i in new_sides:
                if not isinstance(i, int):
                    flag = False
                    break
                else:
                    flag = True
        return flag

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) == True:
            self.__sides = list(new_sides * 12)
            print('Изменятся ', end='')
        else:
            print('Не изменятся ', end='')
        return self.__sides

    def get_volume(self):
        volume = self.get_sides()[0] ** 3
        return volume


circle1 = Circle((200, 200, 100), 10)  # (цвет, стороны)
print(f'Цвет circle1: ', circle1.get_color())
# print(circle1.get_sides())
cube1 = Cube((222, 35, 130), 6)
print(f'Цвет cube1: ', cube1.get_color())
# print(cube1.get_sides())

# Проверка изменения цветов
circle1.set_color(55, 66, 77)  # цвет изменится
print(f'цвет circle1: ', circle1.get_color())
cube1.set_color(300, 70, 15)  # цвет не изменится
print(f'цвет cube1: ', cube1.get_color())

# figure = Figure((245, 28, 19), 10, 15, 6)
# print(figure.get_color())
# print(figure.get_sides())
# figure.set_color(0, 0, 0)
# print(figure.get_color())
triangle = Triangle((250, 20, 40), 15, 9, 8)
print(f'Цвет triangle1: ', triangle.get_color())
print(f'Стороны triangle1:', triangle.get_sides())
# triangle.set_sides(5, 3, 12, 4)
# print(triangle.get_sides())
triangle.set_color(100, 70, 15)
print(f'цвет triangle1:', triangle.get_color())

# Проверка на изменение сторон
print(f'Стороны cube1:', cube1.get_sides())
cube1.set_sides(5, 3, 12, 4, 5)  # не изменится
print(f'стороны cube1:', cube1.get_sides())
cube1.set_sides(15)
print(f'cтороны cube1:', cube1.get_sides())
print(f'Сторона circle1:', circle1.get_sides())
circle1.set_sides(15)  # изменится
print(f'cторона circle1:', circle1.get_sides())
# Длина окружности, радиус и площадь круга
print(f'Длина окружности:', len(circle1))
print(f'Радиус circle1:', circle1._Circle__radius)
print(f'Площадь круга:', circle1.get_square())
# Площадь треугольника
print(triangle.get_square())
# Объём куба
print(f'Объём cube1 =', cube1.get_volume())
# print(dir(circle1))
# print(dir(triangle))
# print(dir(cube1))
# print(dir(figure))

