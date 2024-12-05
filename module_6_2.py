class Vehicle:
    # Список допустимых цветов для окрашивания
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    # Инициализация атрибутов объекта
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner      # Владелец транспорта (может меняться)
        self.__model = model    # Модель транспорта (нельзя менять)
        self.__engine_power = int(engine_power) # Мощность двигателя (нельзя менять)
        self.__color = color    # Мощность двигателя (нельзя менять)

    def get_model(self):
        # Возвращает строку с моделью транспорта
        return print("Модель: ", self.__model)

    def get_power(self):
        # Возвращает строку с мощностью двигателя
        return print("Мощность двигателя: ", self.__engine_power)

    def get_color(self):
        # Возвращает строку с цветом транспорта
        return print("Цвет: ", self.__color)

    def print_info(self):
        # Печатает информацию о транспорте
        self.get_model()    # Печатаем модель
        self.get_power()    # Печатаем мощность
        self.get_color()    # Печатаем цвет
        print("Владелец: ", self.owner, "\n")   # Печатаем владельца

    # Метод для изменения цвета транспорта
    def set_color(self, new_color):
        # Проверяем, есть ли новый цвет в списке допустимых
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color    # Меняем цвет, если он допустим
        else:
            print("Нельзя сменить цвет на", new_color, "\n")   # Ошибка

class Sedan(Vehicle):
    # Ограничение на количество пассажиров в седане
    __PASSENGERS_LIMIT = 5

# Исходный код:
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Печатаем изначальные свойства
vehicle1.print_info()

vehicle1.set_color('Pink')  # Попытка сменить цвет на недопустимый
vehicle1.set_color('BLACK') # Смена цвета на допустимый
vehicle1.owner = 'Vasyok'   # Меняем владельца

vehicle1.print_info()       # Проверяем, что поменялось
