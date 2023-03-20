# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

from random import randint

my_list = [randint(-10, 10) for _ in range(10)]
match_count = 0
match_string = ''
print(my_list)

for i in range(len(my_list) - 1):
    if my_list[i + 1] > my_list[i]:
        match_count += 1
        match_string += f'{my_list[i]} < {my_list[i + 1]}, '
print(f'{match_count} совпадений(я): {match_string}')

# Вариант: создание отфильтрованного списка
new_list = [i for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)
