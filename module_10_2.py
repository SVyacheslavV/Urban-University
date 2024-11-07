import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        battle_days = 0
        warriors = 100
        print(f'{self.name}, на нас напали')
        while warriors > 0:
            time.sleep(1)
            battle_days += 1
            if battle_days % 10 == 1:
                day = 'день'
            elif battle_days % 10 in [2, 3, 4]:
                day = 'дня'
            else:
                day = 'дней'
            warriors -= self.power
            print(f'{self.name} сражался {battle_days} {day}, осталось {warriors} воинов')
        if warriors <= 0:
            print(f'{self.name} одержал победу спустя {battle_days} {day}')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

if first_knight.is_alive() == False and second_knight.is_alive() == False:
    print('Все битвы закончились')
