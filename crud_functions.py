import sqlite3

connection = sqlite3.connect('data_product.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')


def initiate_db(title, description, price):
    check_product = cursor.execute(f'SELECT * FROM Products WHERE title = ?', (title,))
    check = (check_product.fetchone())
    # print(check) # выведет None если нет ел. с таким значением или сам элемент
    if check is None:
        cursor.execute(f'INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
                       (title, description, price))
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products


data_all = get_all_products()

# for el in data_all:
#         print(el)


'''Добавление данных в таблицу'''
for i in range(1, 5):
    initiate_db(f'Продукт {i}', f'Описание {i}', f'{i * 100}')

connection.commit()
connection.close()
