class House: # Создаем объект для многоэтажек
    # имеющий две характеристики: "Наименование" и "Этажность" здания
    def __init__(self, name, number_of_floors):
        self.name = name    # Наименование здания
        self.number_of_floors = number_of_floors    # его этажность

    def go_to(self, new_floor): # Создаём метод проезда до этажа
        print(f'\n"Здание: "{self.name}", едем до {new_floor} этажа')
        # Проверяем, существует ли такой этаж в указанном здании
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует") # Если этажа не существует
        else:
            for floor in range(1, new_floor + 1):
                # Если существует этаж выводим их на экран
                if floor < new_floor:
                    print("Проезжаем этаж: ", floor)
                else:
                    print("Конечный этаж:  ", floor)

h1 = House('ЖК Горский', 18)        # Создаём первый объект с характеристиками
h2 = House('Домик в деревне', 2)    # Создаём второй объект с характеристиками

h1.go_to (5)    #   Нужно проехать до 5 этажа в первом объекте
h2.go_to (10)   #   Нужно проехать до 10 этажа во втором объекте