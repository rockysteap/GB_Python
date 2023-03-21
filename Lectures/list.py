# # Списки
# list_1 = []  # инициализация списка
# list_1 = list()  # инициализация списка
# list_1 = [1, 2, 3, 8]  # инициализация списка
# print(list_1)  # вывод элементов списка в стандартном виде [1, 2, 3, 8]
# print(*list_1)  # вывод элементов списка в виде 1 2 3 8

# for i in list_1:  # вывод элементов списка с помощью цикла
#     print(i)

# print(len(list_1))  # вывод длины списка

# print(list_1[-1])  # вывод последнего элемента по индексу

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)  # добавление элемента
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)  # добавление элемента с помощью цикла
#     print(list_1)

# list_1 = [12, 7, -1, 21, 0]
# # print(list_1.pop())  # удаляет последний элемент
# # a = list_1.pop()  # .pop() удаляет и возвращает элемент
# # print(list_1)
# # print(a)
#
# print(list_1.pop(0))  # удаляет элемент по индексу
# print(list_1)
#
# list_1.insert(2, 11)  # вставка во 2 индекс элемента 11
# print(list_1)

list_1.remove(5)  # удаляет из списка первую найденную 5

# Срезы списков
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])                        # 1
print(list_1[1])                        # 2
print(list_1[len(list_1) - 1])          # 10
print(list_1[-1])                       # 10
print(list_1[-5])                       # 6
print(list_1[:])                        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])                       # [1, 2]
print(list_1[len(list_1)-2:])           # [9, 10]
print(list_1[2:9])                      # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])                    # []
print(len(list_1))
print(list_1[0:len(list_1):6])          # [1, 7]
print(list_1[::6])                      # [1, 7]
