# списки строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# зададим список first_result, сод. длины строк из first_strings
# если длина строки не менее 5 символов
first_result = [len(string) for string in first_strings if len(string) >= 5]

# зададим список second_result, сод. пары слов (кортежи) одинаковой длины
# использ. 2 вложенных цикла for
second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]

# зададим словарь third_result, где ключ -строка, знач. - её длина
# условие записи пары в словарь - чётная длина строки
# объединим списки first_strings и second_strings для перебора
third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

# вывод рез-та
print(first_result)
print(second_result)
print(third_result)