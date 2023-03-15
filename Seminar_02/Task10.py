# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

num = int(input('Введите число: '))
fib_n1 = 0
fib_n2 = 1
index = 1
while fib_n2 <= num:
    if fib_n2 == num:
        print(index)
        break
    fib = fib_n1
    fib_n1 = fib_n2
    fib_n2 += fib
    index += 1
else:
    print(-1)
