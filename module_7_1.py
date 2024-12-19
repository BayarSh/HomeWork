class Product:
    def __init__(self, name, weight, category):
        # Инициализация объекта продукта с его именем, весом и категорией
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # Определение строкового представления продукта
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'  # Имя файла для хранения продуктов

    def get_products(self):
        try:
            # Чтение всех продуктов из файла
            file = open(self.__file_name, 'r')
            return file.read()  # Возвращаем содержимое файла как строку
        except FileNotFoundError:
            # Если файл не найден, возвращаем сообщение
            return "Файл не найден."

    def add(self, *products):
        # Получение существующих продуктов из файла
        existing_products = self.get_products().strip().split('\n')  # Удаляем лишние пробелы и разбиваем на строки

        for product in products:
            # Проверяем, существует ли продукт в списке существующих продуктов
            found = False
            for line in existing_products:
                if product.name in line:
                    found = True
                    break
            if found:
                print(f'Продукт {product.name} уже есть в магазине')  # Сообщение о том, что продукт уже существует
            else:
                # Если продукт не существует, добавляем его в файл
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')  # Записываем новый продукт в файл
                file.close()

# Пример работы программы
if __name__ == "__main__":
    s1 = Shop()  # Создаем экземпляр магазина

    # Создаем несколько продуктов
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')  # Продукт с тем же именем, что и p1

    print(p2)  # Вывод информации о продукте p2

    s1.add(p1, p2, p3)  # Добавляем продукты в магазин

    print(s1.get_products())  # Вывод всех продуктов из магазина