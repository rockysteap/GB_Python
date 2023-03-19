from random import randint


def get_poly(max_power, const_range_min, const_range_max):
    pow_max, c_min, c_max = max_power, const_range_min, const_range_max
    poly = dict()
    for exp in range(pow_max, -1, -1):
        poly.setdefault(exp, randint(c_min, c_max))
    return poly


def print_poly(poly, x):
    poly_string = ''
    max_key = 0
    for key in poly:
        if key > max_key:
            max_key = key
    for key, value in poly.items():
        if value == 0:
            poly_string += ''
        elif value < -1:
            if key > 1:
                poly_string += f'{"-" if key == max_key else " - "}{abs(value)}{x}^{key}'
            if key == 1:
                poly_string += f'{"-" if key == max_key else " - "}{abs(value)}{x}'
            if key == 0:
                poly_string += f'{"-" if key == max_key else " - "}{abs(value)}'
        elif value == -1:
            if key > 1:
                poly_string += f'{"-" if key == max_key else " - "}{x}^{key}'
            if key == 1:
                poly_string += f'{"-" if key == max_key else " - "}{x}'
            if key == 0:
                poly_string += f'{"-" if key == max_key else " - "}'
        elif value == 1:
            if key > 1:
                poly_string += f'{"" if key == max_key else " + "}{x}^{key}'
            if key == 1:
                poly_string += f'{"" if key == max_key else " + "}{x}'
            if key == 0:
                poly_string += f'{"" if key == max_key else " + "}'
        elif value > 1:
            if key > 1:
                poly_string += f'{"" if key == max_key else " + "}{value}{x}^{key}'
            if key == 1:
                poly_string += f'{"" if key == max_key else " + "}{value}{x}'
            if key == 0:
                poly_string += f'{"" if key == max_key else " + "}{value}'
    return poly_string


def add_poly(poly1, poly2):
    res_poly = dict()
    poly1_max_key, poly2_max_key = 0, 0
    for key in poly1:
        if key > poly1_max_key:
            poly1_max_key = key
    for key in poly2:
        if key > poly2_max_key:
            poly2_max_key = key
    pow_max = poly1_max_key
    if poly2_max_key > poly1_max_key:
        pow_max = poly2_max_key
    for i in range(pow_max, -1, -1):
        val = poly1.get(i, 0) + poly2.get(i, 0)
        res_poly.setdefault(i, val)
    return res_poly
