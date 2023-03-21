# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
import random
import string

# # 1 способ
# input_str = input('Введите строку: ')
# # input_str = 'beleberda'  # отладка)
# my_list = list(input_str)
# # print(my_list)
#
# my_dict = dict()
# for item in set(my_list):
#     my_dict.setdefault(item, 0)
#
# # print(my_dict)
#
# for key, value in my_dict.items():
#     for i in range(len(my_list)):
#         if my_list[i] == key:
#             if value > 0:
#                 my_list[i] = f'{key}_{value}'
#             value += 1
#
# result_str = ''
# for i in my_list:
#     result_str += f'{i} '
# print(result_str)


# # 2 способ
# in_str = input('Введите строку: ')
# my_dict = dict()
# for i in in_str:
#     if i in my_dict:
#         print(f'{i}_{my_dict[i]}', end=' ')
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
#         print(i, end=' ')
# print(my_dict)

# # 3 способ
# my_string = ''.join([random.choice(string.ascii_letters) for i in range(30)])
#
# dict_count = {}
# for char in my_string:
#     dict_count[char] = dict_count.get(char, 0) + 1
#     if dict_count.get(char) > 1:
#         print(f'{char}_{dict_count.get(char)} ', end='')
#     else:
#         print(char + ' ', end='')


# 3-a способ со сбором строки
my_string = ''.join([random.choice(string.ascii_letters) for i in range(30)])

dict_count = {}
result_str = ''
for char in my_string:
    dict_count[char] = dict_count.get(char, 0) + 1
    if dict_count.get(char) > 1:
        result_str += f'{char}_{dict_count.get(char)} '
    else:
        result_str += char + ' '
print(result_str)
