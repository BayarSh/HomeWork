# Определяем количество участников в командах
team1_num = 5   # Количество участников в команде Мастера кода
team2_num = 6   # Количество участников в команде Волшебники данных
score_1 = 40    # Количество задач, решённых командой Мастера кода
score_2 = 42    # Количество задач, решённых командой Волшебники данных
team1_time = 1552.512  # Время, затраченное командой Мастера кода на решение задач
team2_time = 2153.31451  # Время, затраченное командой Волшебники данных на решение задач
tasks_total = 82  # Общее количество решённых задач

# Форматируем строку с использованием оператора %
output1 = "В команде Мастера кода участников: %d !" % team1_num
print(output1)
output2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(output2)

# Использование format()
output3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(output3)
output4 = "Волшебники данных решили задачи за {} с !".format(round(team2_time,1))
print(output4)

print(f"Команды решили {score_1} и {score_2} задач.")

# Определение победителя
challenge_result = 'Победила команда: '
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'{challenge_result} {result}') # Вывод результата

# Вычисление общего количества решенных задач
tasks_total = score_1 + score_2
# Вычисление общего времени на решения всех задач
time_total = team1_time + team2_time
# Среднее время решения задач
time_avg = round(time_total / tasks_total, 1)
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")

