# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
import random

my_list = [random.randint(1, 5) for i in range(20)]
print(my_list)

dict_count = dict()
for item in my_list:
    dict_count[item] = dict_count.get(item, 0) + 1
print(dict_count)
pairs = 0
for item in dict_count.values():
    pairs += item // 2
print(f'Всего пар: {pairs}.')
