def all_variants(text):
    n = 0
    while n != len(text):
        for i in range(len(text)):
            letter = text[i: i + n + 1]
            if i + n + 1 > len(text):
                continue
            yield letter
        n += 1


a = all_variants('abc')
for i in a:
    print(i)
