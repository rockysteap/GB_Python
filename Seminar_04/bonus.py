# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырехзначных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

from random import randint
# 1 этап
my_list = [randint(1000, 9999) for i in range(7)]
print(f'1 этап: {my_list}')

# 2 этап
num = int(input('2 этап: Введите цифру: '))
for index in range(len(my_list)):
    if str(num) in str(my_list[index]):
        my_list[index] = int(str(my_list[index]).replace(str(num), ''))
print(f'2 этап: {my_list}')

# 3 этап
for index in range(len(my_list)):
    while len(str(my_list[index])) > 1:
        summa = 0
        for item in str(my_list[index]):
            summa += int(item)
        my_list[index] = summa
print(f'3 этап: {my_list}')

# 4 этап
my_list = list(set(my_list))
print(f'4 этап: {my_list}')
