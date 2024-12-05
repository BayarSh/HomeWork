import time


class User:
    def __init__(self, nickname, password, age):
        # Конструктор класса User инициализирует имя пользователя, пароль и возраст
        self.nickname = nickname
        self.password = password  # Храним пароль в открытом виде
        self.age = age

    def __str__(self):
        # Строковое представление пользователя
        return f"User   (nickname={self.nickname}, age={self.age})"

    def __eq__(self, other):
        # Метод для сравнения пользователей по имени
        return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        # Конструктор класса Video инициализирует заголовок, длительность и возрастное ограничение
        self.title = title
        self.duration = duration
        self.time_now = 0  # Текущая секунда воспроизведения, изначально 0
        self.adult_mode = adult_mode  # Ограничение по возрасту

    def __str__(self):
        # Строковое представление видео
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

    def __eq__(self, other):
        # Метод для сравнения видео по заголовку
        return self.title == other.title


class UrTube:
    def __init__(self):
        # Конструктор класса UrTube инициализирует списки пользователей и видео, а также текущего пользователя
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        # Метод для входа пользователя
        for user in self.users:
            # Проверяем, существует ли пользователь с таким никнеймом и паролем
            if user.nickname == nickname and user.password == password:
                self.current_user = user  # Устанавливаем текущего пользователя
                return
        print("Пользователь не найден или неправильный пароль.")

    def register(self, nickname, password, age):
        # Метод для регистрации нового пользователя
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")  # Проверяем на уникальность никнейма
        else:
            new_user = User(nickname, password, age)  # Создаем нового пользователя
            self.users.append(new_user)  # Добавляем пользователя в список
            self.current_user = new_user  # Автоматически входим под новым пользователем

    def log_out(self):
        # Метод для выхода пользователя
        self.current_user = None

    def add(self, *videos):
        # Метод для добавления видео
        for video in videos:
            # Проверяем, существует ли видео с таким же заголовком
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)  # Добавляем видео в список

    def get_videos(self, keyword):
        # Метод для поиска видео по ключевому слову
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    def watch_video(self, title):
        # Метод для воспроизведения видео
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")  # Проверка на вход в аккаунт
            return

        for video in self.videos:
            if video.title == title:
                # Проверка на возрастное ограничение
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                # Воспроизведение видео
                while video.time_now < video.duration:
                    print(video.time_now + 1)  # Вывод текущей секунды
                    video.time_now += 1
                    time.sleep(1)  # Задержка на 1 секунду
                print("Конец видео")  # Сообщение о завершении видео
                video.time_now = 0  # Сбрасываем время воспроизведения
                return

        print("Видео не найдено.")  # Если видео не найдено


# Код для проверки
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)  # Создание видео
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)  # Видео с возрастным ограничением

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # Поиск по ключевому слову
print(ur.get_videos('ПРОГ'))  # Поиск по другому ключевому слову

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Попытка воспроизведения без входа
ur.register('vasya_pupkin', 'lolkekcheburek', 13)  # Регистрация пользователя
ur.watch_video('Для чего девушкам парень программист?')  # Попытка воспроизведения с ограничением по возрасту
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Регистрация пользователя старше 18
ur.watch_video('Для чего девушкам парень программист?')  # Воспроизведение видео

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Попытка регистрации с существующим никнеймом
print(ur.current_user)  # Проверка текущего пользователя

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  # Попытка воспроизведения видео, которого нет