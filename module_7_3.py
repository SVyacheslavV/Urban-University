from pprint import pprint


class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for el in args:
            self.file_names.append(el)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                string = ''
                text = []
                for line in file:
                    string += line.lower()
                string = string.split()
                for el in string:
                    text.append(el.strip(',.=!?;:-'))
            key = name
            value = text
            all_words[key] = value
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            key = name
            value = words.index(word.lower()) + 1
            result[key] = value
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            key = name
            value = words.count(word.lower())
            result[key] = value
        return result


# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
