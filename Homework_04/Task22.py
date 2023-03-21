# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
in_tuple = tuple(input('Введите через пробел длины двух коллекций: ').split())
my_list1 = [randint(0, 20) for _ in range(int(in_tuple[0]))]
my_list2 = [randint(0, 20) for _ in range(int(in_tuple[1]))]
print(my_list1)
print(my_list2)
print(sorted(set(my_list1).intersection(set(my_list2))))
