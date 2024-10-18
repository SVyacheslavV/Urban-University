import time


class User:
    '''Класс пользователя, содержит атрибуты: имя, пароль, возраст'''

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)


class Video:
    '''Класс видео содержит атрибуты: заголовок, продолжительность, секунда остановки,
    ограничение по возрасту'''

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    '''Класс содержит атрибуты: список пользователей, список видео, текущий пользователь'''

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            flag = True
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f'{self.current_user.nickname} текущий пользователь')
                break
            elif user.nickname == nickname and user.password != password:
                print(f'Не верный пароль для пользователя {nickname}')
                break
            else:
                flag = False
        if flag == False:
            print(f'Пользователь {nickname} не найден')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                return print(f'Пользователь {nickname} уже существует')
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None
        print(f'Текущий пользователь {self.current_user}')

    def add(self, *args):
        for i in args:
            for video in self.videos:
                if i.title == video.title:
                    flag = True
                    break
                if i.title != video.title:
                    flag = False
            if len(self.videos) == 0 or flag == False:
                self.videos.append(i)
        return self.videos

    def get_videos(self, word):
        result = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, name):
        for video in self.videos:
            if name == video.title:
                if self.current_user == None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif video.adult_mode == True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(1, video.duration + 1):
                        time.sleep(1)
                        print(i, end=" ")
                        if i == video.duration:
                            print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# v3 = Video('Лучший язык программирования 2024 года', 200)
# v4 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
# ur.add(v1, v2, v3, v4)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJCIb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# ur.watch_video('Лучший язык программирования 2024 года')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

ur.log_in('vasya', 8584848484)
ur.log_in('vasya_pupkin', 48484848484)
ur.log_in('vasya_pupkin', hash('lolkekcheburek'))
ur.log_out()
