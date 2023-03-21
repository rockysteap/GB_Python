# # Словари

# d = {}  # инициализация dict
# d = dict()  # инициализация dict
#
# d['q'] = 'q'
# print(d)
# print(type(d))
#
# d['w'] = 'w'
# print(d)

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
#
# # типы ключей могут отличаться
# dictionary[99] = 999  # добавили и ключ и значение int
# dictionary[98] = 'NinetyEight'  # добавили ключ int значение string
# print(dictionary)
# print(dictionary['up'])  # ↑
#
# print(dictionary['left'])  # ←
# dictionary['left'] = '⇐'  # изменение значения по ключу
# print(dictionary['left'])  # ⇐
#
# # print(dictionary['type'])  # KeyError: 'type' - такого ключа нет
#
# del dictionary['left'] # удаление элемента

# for item in dictionary: print(item)  # печатает ключи
# for (k, v) in dictionary.items(): print(k, v)  # печатает пары ключ-значение

# for item in my_list:
#     count_dict[item] = count_dict.get(item, 0) + 1
