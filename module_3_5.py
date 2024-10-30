def get_multiplied_digits(number):
    str_number = str(number)    # Преобразуем аргумент в строку
    first = int(str_number[0])  # Получаем первую цифру как число
    if len(str_number) > 1:
        # Умножаем первую цифру на результат для оставшихся цифр
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки 1, возвращаем первую цифру
        return first


result = get_multiplied_digits(40203)
print(result)