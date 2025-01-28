import time
class User:
    """
    Атрибуты:
        nickname - имя пользователя, строка,
        password - в хэшированном виде, число,
        age - возраст, число.
    """
    lst_videos = []
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    """
    Атрибуты:
        title - заголовок, строка,
        duration - продолжительность, секунды,
        time_now - секунда остановки (изначально 0),
        adult_mode - ограничение по возрасту, bool (False по умолчанию).
    """

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    """
    Атриубты:
        users - список объектов User,
        videos - список объектов Video,
        current_user - текущий пользователь, User

    Методы:
        log_in - принимает на вход аргументы: nickname, password и пытается найти пользователя
              в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется
              на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        register - принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
              если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь
              {nickname} уже существует". После регистрации, вход выполняется автоматически.
        log_out - сбрасывает текущего пользователя на None.
        add - принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
              названием видео ещё не существует. В противном случае ничего не происходит.
        get_videos - принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
              слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
        watch_video - который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
              то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
              После текущее время просмотра данного видео сбрасывается.
    """
    users = []
    videos = []
    current_user = None

    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def __new__(cls, *args, **kwargs):
        super().__new__(cls)



    # def log_in(self):
    #
    # def log_out(self):
    #
    # def register(self):
    #         if self.nickname in users:
    #             print(f'Пользователь {nickname} уже существует.')
    #
    # def add(self, *videos):
    #     self.lst_videos.append(videos)
    #
    # def get_videos(self):
    #
    # def watch_video(self):


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

print(v1.__dict__)
print(ur.__dict__)

# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
