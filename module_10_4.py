from queue import Queue
import threading
import time
from random import randint


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    def __init__(self, queue, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:  # перебираем список гостей
            for table in tables:  # перебираем список столов
                if table.guest is None:  # если за столом никого нет
                    flag = True
                    table.guest = guest  # присваиваем столу гостя
                    guest.start()  # запускаем поток гостя
                    print(f'{guest.name} сел(а) за стол номер {table.number}')
                    break
                else:
                    flag = False
            if flag == False:  # если все столы заняты
                self.queue.put(guest)  # ставим гостя в очередь
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        counter = 0  # количество пустых столов
        while counter != len(tables):  # пока количество пустых столов не равно количеству столов
            for table in tables:
                # if table.guest == None:
                #     continue
                # if table.guest.is_alive() == False:  # если поток гостя остановлен
                #     print(f'{table.guest.name} покушал(а) и ушёл(ушла)')
                #     print(f'Стол номер {table.number} свободен')
                #     table.guest = None  # присваиваем значение None
                #     counter += 1
                #     if not self.queue.empty():  # если очередь не пустая
                #         guest = self.queue.get()
                #         print(f'{guest.name} вышел(ла) из очереди и сел(а) за стол номер {table.number}')
                #         table.guest = guest
                #         guest.start()
                #         counter -= 1

                try: # с обработкой исключений
                    if table.guest.is_alive() == False:  # если поток гостя остановлен
                        print(f'{table.guest.name} покушал(а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None  # присваиваем значение None
                        counter += 1
                        if not self.queue.empty():  # если очередь не пустая
                            guest = self.queue.get()
                            print(f'{guest.name} вышел(ла) из очереди и сел(а) за стол номер {table.number}')
                            table.guest = guest
                            guest.start()
                            counter -= 1
                except AttributeError:
                    continue

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtag', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
