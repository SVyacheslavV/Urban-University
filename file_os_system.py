import os
import time

print('Текущая директория:', os.getcwd())
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join('.', file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(__file__)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
              f' {formatted_time}, Родительская директория: {parent_dir}')

# C:\Users\user\PycharmProjects\Urban_University\.venv\Scripts\python.exe C:\Users\user\PycharmProjects\Urban_University\.venv\module_7\directory\file_os_system.py
# Текущая директория: C:\Users\user\PycharmProjects\Urban_University\.venv\module_7\directory
# Обнаружен файл: file_os_system.py, Путь: .\file_os_system.py, Размер: 656 байт, Время изменения: 28.10.2024 18:39, Родительская директория: C:\Users\user\PycharmProjects\Urban_University\.venv\module_7\directory
# Обнаружен файл: __init__.py, Путь: .\__init__.py, Размер: 0 байт, Время изменения: 28.10.2024 18:18, Родительская директория: C:\Users\user\PycharmProjects\Urban_University\.venv\module_7\directory

# Process finished with exit code 0
