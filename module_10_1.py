from pprint import pprint
import threading
import time
import datetime


def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(1, word_count + 1):
        file.write(f'Какое-то слово № {i}\n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


# start_write = time.time() # если используем time
start_write = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# end_write = time.time() # если используем time
end_write = datetime.datetime.now()
time_wtite = end_write - start_write
print(f'Работа потоков {time_wtite} секунд(ы)')

# start_write = time.time()
start_write = datetime.datetime.now()

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

# end_write = time.time()
end_write = datetime.datetime.now()
time_wtite = end_write - start_write
print(f'Работа потоков {time_wtite} секунд(ы)')
