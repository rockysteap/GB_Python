# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10^5.
# Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).
import time

# n = 220
# m = 284
start = time.time()


def get_divisors_sum(num: int) -> int:
    divisors_sum = 0
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            divisors_sum += divisor + num // divisor
    return divisors_sum + 1


# print(get_divisors_sum(n))
# print(get_divisors_sum(m))


for num in range(0, 1_000_000):
    first_sum = get_divisors_sum(num)
    second_sum = get_divisors_sum(first_sum)
    if second_sum == num and first_sum != second_sum:
        print(num, first_sum)

finish = time.time()
print(round(finish-start))
