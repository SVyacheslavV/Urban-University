class Vehice:
    __COLOR_VARIANT = ['white', 'black', 'blue', 'green', 'red']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner  # str
        self.__model = __model  # str
        self.__engine_power = int(__engine_power)  # int
        self.__color = __color  # str

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощьность: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        # print(self.get_color())
        print(self.get_model() + '\n' + self.get_horsepower() + '\n' + self.get_color() + '\n' + 'Владелец:',
              self.owner)

    def set_color(self, new_color):
        self.new_color = new_color
        if self.new_color.lower() in self.__COLOR_VARIANT:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')


class Sedan(Vehice):
    __PASSENGER_LIMIT = 5


# Текущие цета __COLOR_VARIANT = ['white', 'black', 'blue', 'green', 'red']
vehile1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehile1.print_info()
vehile1.set_color('Pink')
vehile1.set_color('BLACK')
vehile1.owner = 'Vasyok'
vehile1.print_info()
