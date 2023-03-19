# Ввести натуральную степень k и создать на основе этой степени многочлен.
# Коэффициенты сформировать случайным образом. Сгенерировать 2 многочлена и сложить их.

from random import randint
import polynomial
# polynomial.py (в той же папке)
# get_poly(max_power, const_range_min, const_range_max) - сгенерировать многочлен и записать в словарь
# print_poly(polynom, constant_name) - переводит словарь в строку для вывода
# add_poly(polynom_1, polynom2) - складывает два многочлена

max_power = int(input('Введите максимально возможную натуральную степень: '))
max_power_1, max_power_2 = randint(2, max_power), randint(2, max_power)
const_range_min, const_range_max = -10, 10

polynom_1 = polynomial.get_poly(max_power_1, const_range_min, const_range_max)
polynom_2 = polynomial.get_poly(max_power_2, const_range_min, const_range_max)
result_polynom = polynomial.add_poly(polynom_1, polynom_2)

print(f"Сформирован 1ый многочлен: {polynomial.print_poly(polynom_1, 'x')}")
print(f"Сформирован 2ой многочлен: {polynomial.print_poly(polynom_2, 'x')}")
print(f"Сумма многочленов равна: {polynomial.print_poly(result_polynom, 'x')}")
