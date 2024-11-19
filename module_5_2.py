class House:    # Создаем объект для многоэтажек
    # имеющий две характеристики: "Наименование" и "Этажность" здания
    def __init__(self, name, number_of_floors):
        self.name = name                            # Наименование здания
        self.number_of_floors = number_of_floors    # его этажность

    def __len__(self):  # Этот метод возвращает количество этажей здания, которое хранится в атрибуте number_of_floors
        return self.number_of_floors

    def __str__(self):  #Этот метод возвращает строку, содержащую название здания и количество этажей в формате, указанном в задаче
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))