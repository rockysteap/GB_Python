# import this

# Дана упорядоченная последовательность an чисел от 1 до N.
# Из копии данной последовательности bn удалили одно число, а оставшиеся перемешали.
# Найти удаленное число.

import random

num = 10
my_list = [_ for _ in range(1, num + 1)]
print(my_list)
my_list_count_before = sum(my_list)
# for i in my_list:
#     my_list_count_before += i

# строчка для 2 варианта
my_set_before = set(my_list)


print(my_list_count_before)
my_list.pop(random.randint(0, num - 1))
random.shuffle(my_list)
my_list_count_after = sum(my_list)
# for i in my_list:
#     my_list_count_after += i

print(my_list)
print(my_list_count_before - my_list_count_after)

# 2 вариант
my_set_after = set(my_list)
print(my_set_before.difference(my_set_after))
