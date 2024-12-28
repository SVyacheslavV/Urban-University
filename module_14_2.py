import sqlite3

connection = sqlite3.connect('not_telegram1.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

'''Добавление данных через цикл'''
# for i in range(1, 11):
#     cursor.execute(' INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#     (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', 1000))

'''Обновление данных элемента'''
# cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 != 0', (500,))

'''Удаление данных'''
# cursor.execute('SELECT COUNT(*) FROM Users') # получаем количество строк в Users
# n = cursor.fetchall()
# for i in range(1, n[0][0] + 1, 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

'''Поиск данных'''
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
# users = cursor.fetchall()  # сохраняем данные в переменную users
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

'''Удаляем данные по id = 6'''
# cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

'''Количество записей'''
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
# print(total_users)

'''Сумма данных в столбце balance'''
cursor.execute('SELECT SUM(balance) FROM Users')  # считаем сумму в столбце balance
all_balance = cursor.fetchone()[0]
# print(all_balance)

'''Среднее значение в столбце balance'''
print(all_balance / total_users)

'''Среднее значение в столбце balance(AVG)'''
cursor.execute('SELECT AVG(balance) FROM Users')  # среднее значение в столбце balance с помощью AVG
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connection.commit()
connection.close()
