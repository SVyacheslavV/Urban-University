calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    result = ((len(string), string.upper(), string.lower()))
    count_calls()
    return result

def is_contains(string, list_to_search):
    count_calls()
    for el in list_to_search:
        if el.lower() == string.lower():
            flag = True
            break
        else:
            flag = False
    return flag

print(string_info('Capibara'))
print(string_info('Armagedon'))
print(string_info('Привет'))
print(is_contains('Urban',['ban', 'BaNan', 'urBAN'])) # matches
print(is_contains('cycle',['recycling', 'cyclec'])) # no matches
print(is_contains('Стол',['СтоЛб', 'сто', 'столик'])) # no matches
print(is_contains('клУб',['Клумба', 'клубок', 'КлуБ'])) # matches
print(calls)