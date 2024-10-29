numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Вводим значения данных в задаче

# Создаем пустые списки для простых и составных чисел
primes = []
not_primes = []

# Цикл для перебора каждого числа в списке
for num in numbers:
    if num == 1:        # Числа 1 не являются простыми
        continue        # Прерываем цикл

    primes_yes = True   # Предполагаем, что выбранное число простое

    # Вложенный цикл для проверки делимости
    for i in range(2, num):
        if int(num % i) == 0:   # Если есть делитель
            primes_yes = False  # Число не простое (составное)
            break               # Прекращаем проверку, так как число не простое

    # В зависимости от значения is_prime добавляем число в соответствующий список
    if primes_yes:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки простых и составных чисел
print(" Простые числа:", primes, "\n", "Не простые (составные) числа:", not_primes)

