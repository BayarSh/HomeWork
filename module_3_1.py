calls = 0       # Назначаем глобальной переменной значение 0

def count_calls():
    global calls    # Используем глобальную переменную, определенную вне функции
    calls += 1      # Увеличиваем количество вызовов функции count_calls

def string_info(string):
    count_calls()   # Вызываем функцию count_calls
    length = len(string)    #
    upper = string.upper()  #
    lower = string.lower()  #
    result = (length, upper, lower) #
    return result           #

def is_contains(string, list_to_search):
    count_calls()   # Вызываем функцию count_calls
    result = False  # Предполагаем, что наличие строки в списке не совпадают - Ложь
    # Приводим строку к нижнему регистру для сравнения
    string_lower = string.lower()
    # Проверяем наличие строки в списке с учетом регистра
    for s in list_to_search:
        if string_lower == s.lower():
            result = True   # Если есть хоть одно совпадение, то результат Истина
            break           # Прерываем цикл
    return result           # Выводим результат

print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False

# Выводим количество вызовов
print(calls)  # 4