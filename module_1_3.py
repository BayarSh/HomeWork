name='Джон' #Присваиваем переменной name строковое значение "Джон'
age=25 #Присваиваем переменной age целое значение 25
print('Имя: '+name) #Выводим результат на экран путем сложения строк
print('Возраст: ',age) #Выводим результат на экран через запятую, так как разные типы данных
age=age+1 #Присваиваем переменной age значение age +1
print('Новая эра: ',age) #Выводим результат на экран через запятую
is_student=True #Присваиваем переменной is_student логическое значение Истина (True)

if is_student: #Если переменная is_student Истина
    print('Является студентом: Верно') #то выводится соотвествующая надпись
else: #Иначе
    print('Является студентом: Нет') #выводится другое сообщение