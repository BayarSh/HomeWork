class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
	    # Проверяем, что шаг не равен нулю
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start # Указатель, который будет отслеживать текущее значение итерации

    def __iter__(self):
        self.pointer = self.start # Сбрасываем указатель на начальное значение
        return self

    def __next__(self):
	    # Проверяем, достигнут ли конец итерации
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration # Если достигнут конец, выдаем исключение StopIteration
        current = self.pointer # Сохраняем текущее значение
        self.pointer += self.step
        return current

# Пример выполняемого кода:
try:
	iter1 = Iterator(100, 200, 0)
	for i in iter1:
		print(i, end=' ')
except StepValueError:
	print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
	print(i, end=' ')
print()

for i in iter3:
	print(i, end=' ')
print()

for i in iter4:
	print(i, end=' ')
print()

for i in iter5:
	print(i, end=' ')
print()