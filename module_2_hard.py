'''Вариант без использования функции'''
n = int(input('Введите любое число от 3 до 20: '))
result = []
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result.append(i)
            result.append(j)
print('result: ', *result)

'''Вариант с функцией'''
def code(n):
    result = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result.append(i)
                result.append(j)
    print('result: ', *result)
print('Введите любое число от 3 до 20: ', end = '')
code(int(input()))
