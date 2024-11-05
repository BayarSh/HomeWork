def calculate_structure_sum(data):
    Sum = 0
    if isinstance(data, dict):
        # Если элемент - это словарь, проходим по ключам и значениям
        for key, value in data.items():
            Sum += calculate_structure_sum(key)  # Считаем сумму для ключа
            Sum += calculate_structure_sum(value)  # Считаем сумму для значения
    elif isinstance(data, (list, tuple, set)):
        # Если элемент - это список(), кортеж[] или множество{} проходим по элементам
        for item in data:
            Sum += calculate_structure_sum(item)
    elif isinstance(data, str):
        # Если элемент - это строка, добавляем её длину
        Sum += len(data)
    elif isinstance(data, (int, float)):
        # Если элемент - это число, добавляем его значение
        Sum += data

    return Sum


# Данные задания
data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99