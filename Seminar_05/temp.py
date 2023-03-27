def fib(num, count):
    count += 1
    print(f'вызов {count}')
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fib(num - 1, count) + fib(num - 2, count)

# print(fib(2))
print(fib(5,0))
# print(fib(10))
# print(fib(11))
