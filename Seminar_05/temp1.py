# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
import time


def is_simple(num: int) -> bool:
    my_list = []
    for i in range(2, num):
        if num % i == 0:
            my_list.append(i)
    if my_list:
        return False
    return True


start = time.time()
print(is_simple(1234165784123))
finish = time.time()
# print(is_simple(777))
# print(is_simple(199))
# print(is_simple(149))

print(finish - start)
