def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

my_list = []
for i in range(1, 10):
    my_list.append(fib(i))
print(my_list)