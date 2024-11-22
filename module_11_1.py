import requests  # работа с http запросами
import pandas as pd  # анализ данных
import matplotlib.pyplot as plt  # визуализация данных (графики)
from PIL import Image # обработка картинок


'''Пример работы с pandas'''

# df = pd.read_csv(
#     'https://drive.google.com/uc?export=download&id=1dLwh-PaDERYQJ32IQHUCCMyaCVdFq4ot',
#     sep=',')
# print(df) # вывод в консоль датасета
# print(df.shape) # размер датасета (row, column)
# print(df.columns) # название (столбцов) датасета
# print(df.dtypes) # тип данных для каждого из столбцов
# print(df.notnull().sum()) # сумма количества значений
# print(df.isnull().sum()) # сумма пропусков
# print(df.info()) # метаданные датасета - совмещает columns, notnull().sum(), dtypes
# print(df.head(8)) # выводит указанное количество первых строк датасета. Если () то выводит первые 5
# print(df.tail()) # тоже что и head(), но вывод с конца датасета

'''Пример работы с matplotlib'''

# Линейные графики
# x_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_1 = []
# for i in x_1:
#     y_1.append(i ** 2)
# x_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y_2 = [80, 75, 70, 65, 60, 55, 50, 45, 40]

# plt.plot(x_1, y_1, color='red', marker='o', markersize=5, label='y=x**2')  # построит линию
# plt.plot(x_2, y_2, color='blue', marker='x', markersize=5)
# plt.legend(loc='lower right', frameon=False)
# plt.show()

# Гистограммы
# Пример 1
# values = [15, 20, 25, 30, 35, 40, 45, 17, 23, 45, 37, 28, 42, 34, 27, 38]
# plt.hist(values, bins=6, edgecolor='black')
# plt.xlabel('values') # ось X
# plt.ylabel('count') # ось Y
# plt.title('Гистограмма') # Название
# plt.show()

# Пример 2
# df = pd.read_csv(
#     'https://drive.google.com/uc?export=download&id=1dLwh-PaDERYQJ32IQHUCCMyaCVdFq4ot',
#     sep=',') # получаем csv по ссылке
# print(df)
# plt.hist(df['Weight'], bins=5, edgecolor='black') # построение диаграммы по Weight
# plt.xlabel('Weight')
# plt.ylabel('count')
# plt.title('Гистограмма')
# plt.show()

'''Пример работы с pillow'''
# загрузка изображений из URL
url = 'https://avatars.mds.yandex.net/i?id=2545398a0a8863477b1a40ad3e19dd76_l-9829431-images-thumbs&n=13'
resp = requests.get(url, stream=True).raw # читаем изображение как данные raw
img = Image.open(resp) # создаём картинку из ответного объекта response (resp)
img.save('lesson_pillow.jpg', 'jpeg') # сохраняем изображение с указанием названия и формата
cropped = img.crop((500, 70, 1050,960)) # обрезаем картинку
cropped.save('lesson_pillow1.jpg')
rotated = cropped.rotate(180) # поворачиваем картинку
rotated.save('lesson_pillow_rotated.jpg')
grayscale = cropped.convert('L') # делаем картинку чёрно-белой
grayscale.save('lesson_black.jpg')