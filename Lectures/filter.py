my_list = [2, 15, 4, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, my_list))
print(res)

parsed_input_1 = list(filter(lambda x: x % 2 == 0, my_list))
print(parsed_input_1)

# одновременное использование map и lambda
parsed_input_2 = list(map(lambda x: (x, x**2), parsed_input_1))
print(parsed_input_2)
