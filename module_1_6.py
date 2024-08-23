my_dict = {'Vika': 2020, 'Lena': 1978, 'Vova': 2003, 'Misha': 1997}
print('My_dict:', my_dict)
print('Value:', my_dict['Vika'])
print('Values not in my_dict:', my_dict.get('Dima'))
my_dict.update({'Grisha': 2015, 'Vera': 1965})
del_name = my_dict.pop('Vova')
print('Delete value:', del_name)
print('Update My_dict:', my_dict)
my_set = {1, 2, 3, True, (1, 2, 3), 3, False, 'a', 2, 'd', 1, True}
print('My_set:', my_set)
my_set.add('world')
my_set.add(7)
my_set.discard(2)
print('New my_set:', my_set)
