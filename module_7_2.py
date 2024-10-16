from pprint import pprint


def custom_write(file_name, strings):
    strings_position = {}
    file = open(file_name, 'a', encoding='utf-8')
    for strings in range(len(info)):
        key = (strings + 1, file.tell())
        value = info[strings]
        strings_position[key] = value
        file.write(info[strings] + '\n')
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
