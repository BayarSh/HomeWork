import random

# Базовый класс Animal, описывающий животных
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0] # Координаты в пространстве
        self.speed = speed      # Скорость передвижения

    def move(self, dx, dy, dz):
        # Изменяем координаты с учетом скорости
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] += dz * self.speed

    def get_cords(self):
        # Выводим координаты в нужном формате
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        # Определяем, атакует ли животное
        if self._DEGREE_OF_DANGER < 5:
            print("Извини, я миролюбивый  (＠＾◡＾)")
        else:
            print("Будь осторожен, я нападу на тебя (‡▼益▼)")

    def speak(self):
        # Выводим звук животного
        print(self.sound)

# Класс Птиц, наследуется от Animal
class Bird:
    beak = True     # Наличие клюва

    def lay_eggs(self):
        # Откладываем яйца
        print(f"Вот для Вас {random.randint(1, 4)} яйца")

# Класс Водное животное, наследуется от Animal
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3   # Уровень опасности для водных животных
    def dive_in(self, dz):
        # Метод для ныряния
        dz = abs(dz)  # Делаем dz положительным
        if self._cords[2] - dz >= 0:
            self._cords[2] -= dz  # Уменьшаем координату Z
        else:
            print("Здесь слишком глубоко, я не могу нырять (ಥ﹏ಥ)")

# Класс Ядовитое животное, наследуется от Animal
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8  # Уровень опасности для ядовитых животных

# Класс Duckbill, описывающий утконоса, наследуется от Bird, AquaticAnimal и PoisonousAnimal
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"  # Звук утконоса

    def __init__(self, speed):
        super().__init__(speed)  # Инициализация родительского класса

db = Duckbill(10)

print(db.live)  # True
print(db.beak)  # True

db.speak()  # Click-click-click
db.attack()  # Be careful, i'm attacking you 0_0

db.move(1, 2, 3)  # Изменяем координаты
db.get_cords()  # X: 10 Y: 20 Z: 30
db.dive_in(6)  # Ныряем
db.get_cords()  # X: 10 Y: 20 Z: 0

db.lay_eggs()  # Откладываем яйца
