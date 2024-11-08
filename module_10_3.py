import threading
from random import randint
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        number_refill = 100  # количество операций пополнения
        while number_refill:  # пока количество операций не равно False (0)
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            summa = randint(50, 500)  # сумма пополнения
            self.balance += summa  # прибавляем сумму пополнения к балансу
            print(f'Пополнение: {summa}. Баланс: {self.balance}')
            number_refill -= 1  # количество осташихся операций пополнения
            time.sleep(0.001)  # задержка перед следующей операцией пополнения

    def take(self):
        number_removal = 100  # количество операций снятия
        while number_removal:  # пока количество операций снятия не равно False (0)
            summa_removal = randint(50, 500)  # сумма снятия
            print(f'Запрос на {summa_removal}')
            if summa_removal > self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire(self)
            else:
                self.balance -= summa_removal  # вычитаем сумму снятия из балансу
                print(f'Снятие: {summa_removal}. Баланс: {self.balance}')
            number_removal -= 1  # количество осташихся операций снятия
            time.sleep(0.001)  # задержка перед следующей операцией снятия


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))  # поток для пополнения
th2 = threading.Thread(target=Bank.take, args=(bk,))  # поток для снятия
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
