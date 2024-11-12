from multiprocessing import Pool
from pprint import pprint
import datetime


def read_info(name):
    all_data = []
    file = open(name, 'r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            break
        all_data.append(line)
    file.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start_read = datetime.datetime.now()
# for name in filenames:
#     read_info(name)
# end_read = datetime.datetime.now()
# time_read = end_read - start_read
# print(time_read) # 0:00:38.310996

if __name__ == '__main__':
    start_read = datetime.datetime.now()
    with Pool(4) as pool:
        result = pool.map(read_info, filenames)
    end_read = datetime.datetime.now()
    time_read = end_read - start_read
    print(time_read)  # 0:01:53.809506
