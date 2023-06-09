# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#            Определите минимальное число монеток, которые нужно перевернуть,
#            чтобы все монетки были повернуты вверх одной и той же стороной.
#            Выведите минимальное количество монет, которые нужно перевернуть.

from random import randint

# coins = int(input('Введите кол-во монеток: '))
coins = randint(1, 100)  # вариант с рандомным количеством

heads = randint(1, coins)
result = tails = coins - heads

if heads < tails:
    result = heads

print(f'Всего монет -> {coins}, лежат решкой -> {tails}, гербом -> {heads}.')
print(f'Перевернем {result} шт.')
