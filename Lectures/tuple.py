# # Кортежи
# t = ()  # инициализация tuple
# print(type(t))  # tuple
#
# t = (1)  # инициализация int
# print(type(t))  # int
#
# t = (1,)  # инициализация tuple
# print(type(t))  # tuple
#
# t = (1, 2)  # инициализация tuple
# print(type(t))  # tuple
#
# v = [1, 8, 9]  # инициализация list
# print(v)  # [1, 8, 9]
# print(type(v))  # list
#
# v = tuple(v)  # инициализация tuple
# print(v)  # (1, 8, 9)
# print(type(v))  # tuple

# множественное присваивание
# a, b = 1, 2
# a = b = 1

# a, b, c = v
# print(a, b, c)  # распаковка кортежа

# t = (1, 2, 3, 5)
# print(type(t))

# for i in t:
#     print(i)  # вывод всех элементов
#
# print()
#
# for i in range(len(t)):
#     print(t[i])  # вывод всех элементов используя индекс

# t[0] = 2  # выдаст ошибку, так как tuple - неизменяемый тип данных
