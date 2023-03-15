# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
flag = True
res = 1
num = int(input('Введите число: '))
print(f'Ряд чисел вида 2^k, не превышающий {num}: ', end="")
while flag:
    print(res, end=" ")
    res *= 2
    if res > num:
        flag = False
