# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного

import random

print('Необходимо ввести -> 1:ListLen1, 2:RandMin, 3:RandMax')
my_vars = (20, 1, 5)  # tuple(map(int, input('Введите числа через пробел -> ').split()))
my_list = [random.randint(my_vars[1], my_vars[2]) for i in range(my_vars[0])]
print(my_list)
count = 0
for i in range(1, my_vars[0] - 1):
    if my_list[i] > my_list[i - 1] and my_list[i] > my_list[i + 1]:
        count += 1
print(f'Количество элементов: {count}')
