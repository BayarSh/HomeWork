first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(first) for first in first_strings if len(first) > 5 ]
second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]
third_result = {string: len(string) for string in (first_strings + second_strings) if len(string)%2 == 0}

print(first_result)
print(second_result)
print(third_result)