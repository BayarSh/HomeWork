class House:    # Создаем объект для многоэтажек
    # имеющий две характеристики: "Наименование" и "Этажность" здания

    houses_history = []  # Атрибут класса для хранения истории

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю
        cls.houses_history.append(args[0])  # Название дома передается как первый аргумент
        return super(House, cls).__new__(cls)  # Создаем новый экземпляр

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name, number_of_floors):
        self.name = name                            # Наименование здания
        self.number_of_floors = number_of_floors    # его этажность

# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)