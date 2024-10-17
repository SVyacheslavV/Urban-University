from pprint import pprint


def custom_write(file_name, info):
    strings_position = {}
    file = open(file_name, 'a', encoding='utf-8')
    for string in range(len(info)):
        key = (string + 1, file.tell())
        value = info[string]
        strings_position[key] = value
        file.write(info[string] + '\n')
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)
