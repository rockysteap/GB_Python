# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
import time
import math


# Не оптимальный вариант, только для маленьких чисел:
def is_simple(num: int) -> bool:
    my_list = []
    for i in range(2, num):
        if num % i == 0:
            my_list.append(i)
    if my_list:
        return False
    return True


# start = time.time()
# print(is_simple(1234165784123)) # остановил после двух суток)
# finish = time.time()
# print(finish - start)


# print(is_simple(777))
# print(is_simple(199))
# print(is_simple(149))


# Оптимальный вариант:
# Отсекаем делители 1, 2 и 3, затем проверяем на четность
# И далее проходим циклом от 3 до (корня из числа + 1)

def simple(num: int) -> bool:
    if num in [1, 2, 3]:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


print(simple(49))
