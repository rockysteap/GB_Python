# # Вариант открытия через переменную -> var = open()
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')  # файл и режим записывается в переменную
# # data = open('file.txt', 'a', encoding='UTF-8')  # можно указать кодировку, по умолчанию win1251
# data.writelines(colors)  # redgreenblue записался подряд без разделителей
# data.close()  # разрыв переменной и файла

# # Вариант открытия через цикл -> with open() as var:
# with open('file.txt', 'w') as data:  # файл и режим записывается в переменную
#     data.write('line 1\n')  # перезаписывает первую строку
#     data.write('line 2\n')  # перезаписывает вторую строку
# # В такой конструкции нет необходимости в закрытии файла

# Чтение из файла
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
