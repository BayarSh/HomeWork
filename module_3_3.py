def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()  # без аргументов
print_params('текст')  # только a
print_params(b=25)  # только b
print_params(c=[1, 2, 3])  # только c
print_params(5, 'текст', False)  # все аргументы

# Распаковка параметров
values_list = (False, {'el1' : 1, 'el2' : 2, 'el3' : 3, 'el4' : 4}, 3.1415926)
values_dict = {'a' : True, 'b' : 1, 'c' : "строка"}
print_params(*values_list)  # распаковка списка
print_params(**values_dict) # распаковка словаря

# Распаковка + отдельные параметры
values_list_2 = (54.32, 'Строка')
print_params(*values_list_2, 2)  # распаковка списка и передача отдельного параметра
