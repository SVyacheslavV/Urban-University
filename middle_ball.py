grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students) # делаем из множества список
students.sort() # сортируем список в алфавитном порядке

# первый способ
middle_ball = {}
for i in range(len(students)): # перебираем каждый элемент списка
    middle_ball[students[i]] = sum(grades[i])/len(grades[i]) # обращаемся к словарю по ключу из списка students со значением из списка grades
print(middle_ball)

# второй способ
middle_ball1 = []  # создаём пустой список
for i in range(len(students)):  # перебираем каждый элемент списка students
    middle_ball1.append((students[i], sum(grades[i]) / len(grades[i]))) # добавляем в пустой список кортежи состоящие из i-го элемента списка students и среднего значения i-го элемента списка gradies
middle_ball1 = dict(middle_ball1) # создаём из списка словарь
print(middle_ball1)

# третий способ
for i in range(len(grades)): # перебераем елементы списка grades
    grades[i] = sum(grades[i])/len(grades[i]) # присваиваем елементу новое значение
middle_ball2 = dict(zip(students,grades)) # упаковываем словарь из двух списков
print(middle_ball2)

