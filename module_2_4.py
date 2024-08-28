numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)): # проходим по всем элементам списка
    if numbers[i] == 1: # если встречаем 1 пропускаем
        continue
    is_prime = True # устанавливаем флаг
    for j in range(2, numbers[i]): # проходим по всем делителям от 2 до numbers[i] - 1
        if numbers[i] % j == 0: # если число из списка делится на делитель без остатка
            not_primes.append(numbers[i]) # добавляем число в список not_primes
            is_prime = False # меняем флаг на False
            break # останавливаем итерацию
    if is_prime == True: # если после предыдущей итерации Флаг = True
        primes.append(numbers[i]) # добавляем число в список primes
print('Primes:', primes)
print('Not_primes:', not_primes)