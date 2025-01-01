import sqlite3

connection = sqlite3.connect('database_14_5.db')
cursor = connection.cursor()

'''Создание таблиц Products и Users'''


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')


initiate_db()

'''Заполнение таблицы Products'''


def initiate_products_db(title, description, price):
    check_product = cursor.execute(f'SELECT * FROM Products WHERE title = ?', (title,))
    check = check_product.fetchone()
    # print(check) # выведет None если нет ел. с таким значением или сам элемент
    if check is None:
        cursor.execute(f'INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
                       (title, description, price))
    connection.commit()


'''Заполнение таблицы Users'''


def initiate_users_db(username, email, age):
    check_username = cursor.execute(f'SELECT * FROM Users WHERE username = ?', (username,))
    check = check_username.fetchone()
    # print(check) # выведет None если нет ел. с таким значением или сам элемент
    if check is None:
        cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                       (username, email, age, 1000))
    connection.commit()


'''Добавление пользователя в таблицу Users'''


def add_user(username, email, age):
    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


'''Проверка наличия пользователя в таблице Users по username'''


def is_included(username):
    check_username = cursor.execute(f'SELECT * FROM Users WHERE username = ?', (username,))
    check = check_username.fetchone()
    if check is None:
        return False
    else:
        return True


'''Получение всех продуктов из Products'''


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products


data_all = get_all_products()

# for el in data_all:
#         print(el)


'''Добавление данных в таблицу Products'''
for i in range(1, 5):
    initiate_products_db(f'Продукт {i}', f'Описание {i}', f'{i * 100}')

'''Добавление данных в таблицу Users'''
for i in range(1, 5):
    initiate_users_db(f'username{i}', f'{i}@email{i}', f'{i * 2}')

connection.commit()
# connection.close()
