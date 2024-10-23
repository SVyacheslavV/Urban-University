def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            print(f'Некоректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        res = personal_sum(numbers)
    except TypeError as exc:
        print('В numbers записан некоректный тип данных')
        i_average = None
    else:
        try:
            i_average = res[0] / (len(numbers) - res[1])
        except ZeroDivisionError as exc:
            i_average = 0
    return i_average


print(f'Результат 1: {calculate_average('1, 2, 3')}')
print(f'Результат 2: {calculate_average([1, 'Строка', 3, 'Ещё строка'])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
