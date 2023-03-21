# q = set()  # инициализация множества (набора)
# colors = {'red', 'green', 'blue'}  # set - уникальное множество
# print(type(colors))  # set
# print(colors)
# colors.add('red')  # ничего не добавилось, так как данное значение уже есть в наборе
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)  # {'red', 'green', 'blue', 'gray'}
# # colors.remove('red')
# # print(colors)  # {'green', 'blue', 'gray'}
# # colors.remove('red')  # KeyError: 'red' - ошибка, так как 'red' уже был удален ранее
# colors.discard('red')  # проверяет, есть ли значение 'red' и если есть - удаляет
# print(colors)
# colors.clear()  # полностью очищает набор, удаляя все элементы
# print(colors)  # set() - пустое множество


# # операции со множествами (наборами)
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8} - копирование в переменную c
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}  - объединение a и b и запись в u
i = a.intersection(b)  # i = {8, 2, 5}  - пересечение a и b и запись в i - дубликаты
dl = a.difference(b)  # dl = {1, 3}  - разница - из a вычли дубликаты b
dr = b.difference(a)  # dr = {13, 21}  - разница - из b вычли дубликаты a
q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13} -

# # замороженное множество (набор)
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)  # frozenset({1, 2, 3, 5, 8})
