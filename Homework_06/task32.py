# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#            (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#        5
#        15
# Вывод: [1, 9, 13, 14, 19]
from random import randint

min_list_val, max_list_val, list_len = -200, 200, 25
print(f'Сгенерирован список в диапазоне от {min_list_val} до {max_list_val} размерностью {list_len} элементов:')
my_list = [randint(min_list_val, max_list_val + 1) for i in range(list_len)]
print(my_list)
my_vars = tuple(map(int, input('Введите через пробел мин и макс для сбора индексов -> ').split()))
# my_vars = (2, 50)

# Вариант 1
print('Вариант 1:', [index for index in range(len(my_list)) if my_vars[0] <= my_list[index] <= my_vars[1]])


# Вариант 2
def get_indices(in_list, in_min, in_max) -> list:
    res_list = list()
    for index in range(len(in_list)):
        res_list.append(index) if in_min <= in_list[index] <= in_max else None
    return res_list


print('Вариант 2:', get_indices(my_list, my_vars[0], my_vars[1]))
