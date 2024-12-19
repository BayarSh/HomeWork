def custom_write(file_name, strings):
    # Создаем пустой словарь для хранения позиций и строк
    strings_positions = {}

    # Открываем файл для записи с кодировкой utf-8
    f = open(file_name, 'w', encoding='utf-8')
    # Инициализируем счетчик строк
    line_number = 1
    # Перебираем строки из списка
    for string in strings:
        # Получаем текущую позицию в байтах перед записью строки
        byte_position = f.tell()
        # Записываем строку в файл с добавлением символа новой строки
        f.write(string + '\n')
        # Сохраняем в словарь кортеж (номер строки, байтовая позиция) как ключ и строку как значение
        strings_positions[(line_number, byte_position)] = string
        # Увеличиваем счетчик строк
        line_number += 1
    # Возвращаем словарь с позициями и строками
    return strings_positions

# Пример использования функции
info = [
    'Text for tell.',  # Первая строка
    'Используйте кодировку utf-8.',  # Вторая строка на русском
    'Because there are 2 languages!',  # Третья строка
    'Спасибо!'  # Четвертая строка на русском
]

# Вызываем функцию и сохраняем результат
result = custom_write('test.txt', info)

# Выводим результат на консоль
for elem in result.items():
    print(elem)
