# Task19
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

from random import randint

# list_len = int(input('Введите длину последовательности: '))
# shift = int(input('Введите величину сдвига: '))
list_len = 20
shift = 5
my_list = [i for i in range(list_len)]
print(my_list)

# 1 вариант
# for i in range(shift):
#     my_list.insert(0, my_list.pop())
# print(my_list)

# 2 вариант
# print(my_list[-shift:] + my_list[:-shift])

# 3 вариант
print('[', end='')
for i in range(len(my_list)):
    print(my_list[i - shift], end=', ')
print('', end='')