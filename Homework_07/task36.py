# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод:                                     # Вывод:
# print_operation_table(lambda x, y: x * y) # 1 2 3 4 5 6
#                                             2 4 6 8 10 12
#                                             3 6 9 12 15 18
#                                             4 8 12 16 20 24
#                                             5 10 15 20 25 30
#                                             6 12 18 24 30 36

# # Версия 2 (вывод с пробелами в зависимости от длины максимального)
def print_operation_table(operation, num_rows=6, num_columns=6):
    row_list, col_list = [x for x in range(1, num_rows + 1)], [y for y in range(1, num_columns + 1)]
    matrix_list = [[operation(row, col) for row in row_list] for col in col_list]
    max_symbols = len(str(num_rows * num_columns)) + 1
    for row in matrix_list:
        for item in row:
            print(str(item).rjust(max_symbols), end='')
        print()


print_operation_table(lambda x, y: x * y)  # 6x6 по умолчанию
print()
print_operation_table(lambda x, y: x * y, 10, 10)  # 10x10

# # Версия 1 (вывод как в задании)
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     row_list, col_list = [x for x in range(1, num_rows + 1)], [y for y in range(1, num_columns + 1)]
#     matrix_list = [[operation(row, col) for row in row_list] for col in col_list]
#     for row in matrix_list:
#         print(*row)
