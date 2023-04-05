# my_string = '1234567890'
# my_string = list(my_string)
#
# # map применяет функцию int() ко всем элементам коллекции
# my_string = list(map(int, list(my_string)))
# print(sum(my_string))


# list_1 = [x for x in range(1, 20)]
# print(list_1)
# с помощью map добавим 10 ко всем элементам списка:
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача:
# C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел.
# Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел?

user_input = '12 55 76 889 12 22'
print(user_input)
# user_input = user_input.split()  # вернет список строк

parsed_input_1 = list(map(int, user_input.split()))
print(parsed_input_1)

# одновременное использование map и lambda
parsed_input_2 = list(map(lambda x: (x, x**2), parsed_input_1))
print(parsed_input_2)