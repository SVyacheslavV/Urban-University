team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451

if score1 > score2 or score1 == score2 and teame1_time < teame2_time:
    result = 'Победа команды Мастер кода!'
if score1 < score2 or score1 == score2 and teame1_time > teame2_time:
    result = 'Победа команды Волшебники данных!'
else:
    result = 'Ничья!'

challenge_result = 'Результат битвы:'
task_total = score1 + score2
time_avg = round((team1_time + team2_time) / (score1 + score2), 1)

"""Использование %"""

print('"В команде Мастера кода участников: %s' % team1_num + '!"')
print('"Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num) + '!"')

"""Использование format()"""

print('"Команда Волшебники данных решила задач: {}!"'.format(score2))
print('"Волшебники данных решили задачи за {} c!"'.format(team1_time))

"""Использование f-строк"""

print(f'"Команды решили {score1} и {score2} задач."')
print(f'"{challenge_result} {result}"')
print(f'"Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!"')
