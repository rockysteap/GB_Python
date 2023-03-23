# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
#            и возводит число А в целую степень B с помощью рекурсии.
#            *Пример:*  A = 3; B = 5 -> 243 (3⁵)
#                       A = 2; B = 3 -> 8

def raise_to_power(a, b):
    if b < 2:
        return a
    return a * raise_to_power(a, b - 1)

print(raise_to_power(2, 16))
print(raise_to_power(3, 5))
print(raise_to_power(15, 2))
