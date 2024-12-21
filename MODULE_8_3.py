class IncorrectVinNumber(Exception):
    # Исключение для некорректного VIN номера.
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    # Исключение для некорректного номера автомобиля
    def __init__(self, message):
        self.message = message


class Car:

    def __init__(self, model, vin, numbers):
        self.model = model          # Модель транспорта
        self.__vin = vin            # Приватный атрибут для VIN номера
        self.__numbers = numbers    # Приватный атрибут для номера автомобиля
        self.__is_valid_vin(vin)    # Вызов проверки VIN номера
        self.__is_valid_numbers(numbers)  # Вызов проверки номера автомобиля


    def  __is_valid_vin(self, vin_number):
        # Проверка корректности VIN номера.
        if not isinstance(vin_number, int):  # Проверка типа данных
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:  # Проверка диапазона
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        # Проверка корректности номера автомобиля.
        if not isinstance(numbers, str):  # Проверка типа данных
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:  # Проверка длины строки
            raise IncorrectCarNumbers('Неверная длина номера')
        return True  # Возвращаем True, если все проверки пройдены


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')