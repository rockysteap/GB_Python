# # def calc1(a, b):
# #     return a + b
# calc1 = lambda a, b: a + b  # лямбда вместо обычной функции
#
# # def calc2(a, b):
# #     return a * b
# calc2 = lambda a, b: a * b  # лямбда вместо обычной функции
#
#
# def math(op, x, y):
#     print(op(x, y))
#
#
# math(calc1, 5, 45)  # передаем одну функцию в качестве аргумента в другую
# math(calc2, 5, 45)  # передаем одну функцию в качестве аргумента в другую
# math(lambda a, b: a + b, 5, 45)  # лямбда в качестве передаваемой функции
# math(lambda a, b: a * b, 5, 45)  # лямбда в качестве передаваемой функции

# В списке хранятся числа.
# Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
my_list = [i for i in range(20)]
print(my_list)
# Решение с использованием спискового включения (list comprehension)
print([(i, i**2) for i in my_list if i % 2 == 0])


def select(f, collection):
    return[f(x) for x in collection]


def where(f, collection):
    return [x for x in collection if f(x)]


res = select(int, my_list)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)
