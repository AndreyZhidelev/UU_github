class UrTube:


class Video:
    """
    Атрибуты:
    title(заголовок, строка),
    duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title: str, duration: int, time_now = 0: int, adult_mode = False: bool):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    """
    Атрибуты:
    nickname(имя пользователя, строка),
    password(в хэшированном виде, число),
    age(возраст, число)
    """

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

