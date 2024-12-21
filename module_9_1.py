def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для хранения результатов
    for func in functions:
        results[func.__name__] = func(int_list)  # Вызываем функцию и сохраняем результат
    return results

# Пример использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))