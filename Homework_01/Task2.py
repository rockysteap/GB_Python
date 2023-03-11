""" Задача 2: Найдите сумму цифр трехзначного числа.
    Примеры: 1) 123 -> 6 (1 + 2 + 3)    2) 100 -> 1 (1 + 0 + 0) """

num = int(input('Введите трехзначное число: '))

digit3 = num // 100
digit2 = num // 10 % 10
digit1 = num % 10

res = digit3 + digit2 + digit1

print(f'{num} -> {res} ({digit3} + {digit2} + {digit1})')
