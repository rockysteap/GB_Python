# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета. Круговые орбиты не учитывайте:
# вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были бы запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
import random

elliplist_of_orbitssis = [(random.randint(1, 10),  random.randint(1, 10)) for x in range(10)]
print(elliplist_of_orbitssis)


def find_farthest_orbit(list_of_orbits):
    new_list = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    mult_list = list(map(lambda x: x[0] * x[1], new_list))
    max_mult = max(mult_list)
    dub_list = [x for x in new_list if x[0] * x[1] == max_mult]

    return dub_list

    # index = mult_list.index(max(mult_list))
    # if mult_list[index] in mult_list:
    #     dub_list.append(mult_list[index])
    # print(new_list)
    # print(mult_list)
    # print(new_list[index])
    # return new_list[index]


print('Полуэллипсы орбиты самой далекой планеты: ', *find_farthest_orbit(elliplist_of_orbitssis))
# find_farthest_orbit(elliplist_of_orbitssis)
