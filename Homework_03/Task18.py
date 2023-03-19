# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#            Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#            В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#            Пример: # 5
#                      1 2 3 4 5
#                      6
#                      -> 5

from random import randint

# my_list_len = int(input('Введите длину списка: '))
# my_num = int(input('Введите искомое число: '))
my_list_len, my_num, left_nearest, right_nearest = 20, randint(0, 100), None, None
my_list = [randint(1, 100) for i in range(my_list_len)]

while my_num in my_list:
    print(f'Искомое число \'{my_num}\' присутствует в списке.')
    break
else:
    for item in sorted(my_list):
        if item < my_num:
            left_nearest = item
        else:
            if not right_nearest:
                right_nearest = item

    output_str = f'Числа \'{my_num}\' нет в списке, '
    if left_nearest is not None and right_nearest is not None:
        if abs(left_nearest - my_num) == abs(right_nearest - my_num):
            output_str += f'ближайшие к нему элементы: {left_nearest} и {right_nearest} ' \
                          f'расположены на одинаковом удалении.'
        elif abs(left_nearest - my_num) < abs(right_nearest - my_num):
            output_str += f'ближайшие к нему элементы: {left_nearest} и {right_nearest}, ' \
                          f'но {left_nearest} расположен ближе.'
        else:
            output_str += f'ближайшие к нему элементы: {left_nearest} и {right_nearest}, ' \
                          f'но {right_nearest} расположен ближе.'
    elif left_nearest is None:
        output_str += f'ближайший к нему элемент: {right_nearest}.'
    else:
        output_str += f'ближайший к нему элемент: {left_nearest}.'

    print(f'Отсортированный список: {sorted(my_list)}.')
    print(output_str)
