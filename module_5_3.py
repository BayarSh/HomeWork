class House:    # Создаем объект для многоэтажек
    # имеющий две характеристики: "Наименование" и "Этажность" здания
    def __init__(self, name, number_of_floors):
        self.name = name                            # Наименование здания
        self.number_of_floors = number_of_floors    # его этажность

    def __len__(self):  # Этот метод возвращает количество этажей здания, которое хранится в атрибуте number_of_floors
        return self.number_of_floors

    def __str__(self):  #Этот метод возвращает строку, содержащую название здания и количество этажей в формате, указанном в задаче
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):  #Этот метод возвращает Истину при равенстве этажностей сравниваемых объектов
        return self.number_of_floors == other.number_of_floors


    def __add__(self, other):
        self.number_of_floors += other
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__

print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

