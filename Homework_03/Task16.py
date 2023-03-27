# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#            Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#            В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#            Пример: # 5
#                      1 2 3 4 5
#                      3
#                      -> 1

from random import randint

# my_list_len = int(input('Введите длину списка: '))
# my_num = int(input('Введите искомое число: '))
my_list_len, my_num, my_num_counter = 20, 3, 0
my_dict = {}
my_dict.setdefault(my_num, 0)
my_list = [randint(1, 10) for i in range(my_list_len)]

for item in my_list:
    if item == my_num:
        # 1 способ - счётчик в переменной
        my_num_counter += 1
        # 2 способ - счётчик в словаре
        my_dict[my_num] += 1
print(f'Сформирован список на {my_list_len} элементов:\n{my_list}')
print(f'1 способ: Искомое число \'{my_num}\' встречается в списке {my_num_counter} раз(а). [счётчик в переменной]')
print(f'2 способ: Искомое число \'{my_num}\' встречается в списке {my_dict[my_num]} раз(а). [счётчик в словаре]')

# 3 способ -> метод count()
print(f'3 способ: Число {my_num} встречается в списке {my_list.count(my_num)} раз(а).')
