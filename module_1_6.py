my_dict = {
    "Иван": 1990,
    "Мария": 1985,
    "Алексей": 1992
} #Создадим переменную my_dict и присвоим ей словарь с несколькими парами «ключ-значение»

print("Словарь my_dict:", my_dict) #Выведем на экран словарь my_dict

#Выведем на экран одно значение для существующего ключа и одно для отсутствующего, используя метод get, чтобы избежать ошибок
print("Год рождения Ивана:", my_dict.get("Иван"))
print("Год рождения для отсутствующего ключа:", my_dict.get("Ольга", "Ключ не найден"))

#Добавим ещё две пары в словарь my_dict
my_dict["Анна"] = 1995
my_dict["Дмитрий"] = 1988
print("Словарь my_dict с добавленными парами:", my_dict)

#Удалим одну из пар по существующему ключу и выведем значение из этой пары
удалённое_значение = my_dict.pop("Мария", "Ключ не найден")
print("\nУдалённое значение:", удалённое_значение)
print("Обновлённый словарь my_dict:", my_dict, "\n\n")

#РАБОТА С МНОЖЕСТВАМИ
#Создадим переменную my_set и присвоим ей множество, состоящее из разных типов данных с повторяющимися значениями
my_set = {1, 2, 2, 3, "Байкал", 5.5, "банан", "Байкал", 3.14, 3.14, 3, 2, 5.5}
print("Множество my_set:", my_set) #Выведем на экран множество my_set (отобразятся только уникальные значения)
#Добавим 2 произвольных элемента в множество my_set, которых ещё нет
my_set.add("апельсин")
my_set.add(42)
print("Изменённое множество my_set:", my_set) #Выведем на экран

my_set.remove('банан')  # Удалим элемент, если он существует
print("\nМножество my_set без 'банан':", my_set) #Выведем на экран

