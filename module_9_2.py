first_string = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_string = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(i) for i in first_string if len(i) > 5]
second_result = [(i, j) for i in first_string for j in second_string if len(i) == len(j)]
third_result = {i: len(i) for i in first_string + second_string if len(i) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
