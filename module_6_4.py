import math

class Figure:
    # Количество сторон фигуры
    sides_count = 0

    def __init__(self, color, *sides):
        # Инициализация защищенных атрибутов
        self._sides = []  # Защищенный атрибут для хранения сторон
        self._color = list(color)  # Защищенный атрибут для хранения цвета
        self.filled = False  # Признак заполнения фигуры

        # Установка сторон фигуры
        if len(sides) == self.sides_count:
            self.set_sides(*sides)  # Установка сторон, если их количество соответствует
        else:
            self.set_sides(*([1] * self.sides_count))  # Установка стандартных сторон

    def get_color(self):
        # Возвращает цвет фигуры
        return self._color

    def _is_valid_color(self, r, g, b):
        # Проверяет, является ли цвет допустимым (значения от 0 до 255)
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        # Устанавливает цвет фигуры, если он допустим
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]

    def _is_valid_sides(self, *new_sides):
        # Проверяет, допустимы ли стороны (должны быть положительными и соответствовать количеству)
        return (len(new_sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in new_sides))

    def get_sides(self):
        # Возвращает стороны фигуры
        return self._sides

    def __len__(self):
        # Возвращает сумму длин сторон
        return sum(self._sides)

    def set_sides(self, *new_sides):
        # Устанавливает стороны фигуры, если они допустимы
        if self._is_valid_sides(*new_sides):
            self._sides = list(new_sides)  # Устанавливаем новые стороны


class Circle(Figure):
    # Класс для круга, количество сторон 1
    sides_count = 1

    def __init__(self, color, *sides):
        # Инициализация круга
        super().__init__(color, *sides)  # Вызов конструктора родительского класса
        self.__radius = self._sides[0] / (2 * math.pi)  # Расчет радиуса

    def get_square(self):
        # Возвращает площадь круга
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        # Устанавливает стороны круга и пересчитывает радиус
        if self._is_valid_sides(*new_sides):
            super().set_sides(*new_sides)  # Вызов метода установки сторон родительского класса
            self.__radius = self._sides[0] / (2 * math.pi)  # Пересчет радиуса


class Triangle(Figure):
    # Класс для треугольника, количество сторон 3
    sides_count = 3

    def __init__(self, color, *sides):
        # Инициализация треугольника
        super().__init__(color, *sides)  # Вызов конструктора родительского класса

    def get_square(self):
        # Возвращает площадь треугольника по формуле Герона
        a, b, c = self._sides  # Стороны треугольника
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь


class Cube(Figure):
    # Класс для куба, количество сторон 12
    sides_count = 12

    def __init__(self, color, side_length, *sides):
        # Инициализация куба
        super().__init__(color, *sides)  # Вызов конструктора родительского класса
        if len(sides) == 0:
            self.set_sides(*([side_length] * self.sides_count))  # Установка сторон куба

    def set_sides(self, *new_sides):
        # Устанавливает стороны куба
        if len(new_sides) == 1:
            side_length = new_sides[0]
            if isinstance(side_length, int) and side_length > 0:
                super().set_sides(*([side_length] * self.sides_count))  # Установка одинаковых сторон
        elif len(new_sides) == self.sides_count:
            if self._is_valid_sides(*new_sides):
                super().set_sides(*new_sides)  # Установка сторон, если они допустимы

    def get_volume(self):
        # Возвращает объем куба
        side = self._sides[0]  # Длина стороны
        return side ** 3  # Объем куба


# Пример использования
circle1 = Circle((200, 200, 100), 10)  # Создание круга с цветом и радиусом
cube1 = Cube((222, 35, 130), 6)  # Создание куба с цветом и длиной стороны

# Установка и получение цвета
circle1.set_color(55, 66, 77)  # Установка нового цвета для круга
print(circle1.get_color())  # Вывод цвета круга
cube1.set_color(300, 70, 15)  # Установка нового цвета для куба
print(cube1.get_color())  # Вывод цвета куба

# Установка и получение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Установка сторон куба
print(cube1.get_sides())  # Вывод сторон куба
circle1.set_sides(15)  # Установка новых сторон для круга
print(circle1.get_sides())  # Вывод сторон круга

# Вывод суммы сторон и объема куба
print(len(circle1))  # Вывод суммы сторон круга
print(cube1.get_volume())  # Вывод объема куба