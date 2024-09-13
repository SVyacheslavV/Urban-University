def calculate_structure_sum(data_structure):
    counter = 0
    for el in data_structure:
        if isinstance(el, (int, float)):
            counter += el
        elif isinstance(el, str):
            counter += len(el)
        elif isinstance(el, (list, tuple, set)):
            counter += calculate_structure_sum(el)
        elif isinstance(el, dict):
            for item in el.items():
                counter += calculate_structure_sum(item)
    return counter


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
