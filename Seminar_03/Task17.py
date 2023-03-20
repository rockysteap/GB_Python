from random import randint
my_list = [randint(-4, 4) for _ in range(10)]
res_list = set(my_list)
print(f'{my_list}')
print(f'В списке {res_list} -> {len(res_list)} yникальных значений.')
# 2 вар
print(len(set(my_list)))