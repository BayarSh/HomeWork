#Создание переменной immutable_var и присвоение ей кортежа:
# Создаем кортеж с элементами разных типов данных
immutable_var = (42, "Hello", 3.14, True)

# Выводим кортеж на экран
print("Кортеж immutable_var:", immutable_var)

#Попытка изменения элементов кортежа immutable_var:
#Кортежи в Python являются неизменяемыми (immutable) структурами данных.
#Это означает, что после их создания мы не можем изменить их содержимое.
# Попытка изменения элемента кортежа вызовет ошибку.

# Например:
# Попытка изменить первый элемент кортежа

#    immutable_var[0] = 100

# Выдает ошибку:
#immutable_var[0] = 100
#IndentationError: unexpected indent

#Объяснение: Кортежи являются неизменяемыми, потому что они предназначены для хранения данных,
# которые не должны изменяться в процессе выполнения программы. Это делает их безопасными для передачи в функции и использования в качестве ключей в словарях.

#Создание изменяемой структуры данных mutable_list:
# Создаем список с несколькими элементами
mutable_list = [1, "World", 2.71, False]
print("\nCписок mutable_list:", mutable_list)

# Изменяем элементы списка
mutable_list[0] = 1000
mutable_list[1] = "Python"
mutable_list[2] = 3.14159
mutable_list[3] = True

# Выводим измененный список на экран
print("Измененный список mutable_list:", mutable_list)
#В отличие от кортежей, списки в Python являются изменяемыми (mutable), что позволяет изменять их содержимое после создания. Вы можете добавлять, удалять или изменять элементы списка.