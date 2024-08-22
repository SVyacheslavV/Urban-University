immutable_var = 'Hello', 1, 2, 3, True # кортеж (tuple) - неизменяемый тип данных
print(immutable_var)
mutable_list = [1, 2, 3.5, 'a', 'b', False] # список (list) - изменяемый тип данных
print(mutable_list)
mutable_list[0] = 'one'
print(mutable_list)
mutable_list[2] = True
print(mutable_list)