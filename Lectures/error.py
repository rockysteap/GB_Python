# # Распространенные ошибки

# # 1. SyntaxError (Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second  # !!!!! отсутствует ':' после условия if
#  print(number_first)
#  # SyntaxError: expected ':' -

# # 2. IndentationError (Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!! отсутствует отступ внутри цикла if
# # IndentationError: expected an indented block after 'if' statement

# # 3. TypeError (Ошибка типов)
# text = 'Python'
# number = 5
# print(text + number)  # !!!!! нельзя складывать строки и числа
# # TypeError: can only concatenate str (not "int") to str

# # 4. ZeroDivisionError (Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)  # !!!!! делить на 0 нельзя
# # ZeroDivisionError: integer division or modulo by zero

# # 5. KeyError (Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])  # !!!!! такого ключа не существует
# # KeyError: 3

# # 6. NameError (Ошибка имени переменной)
# name = 'Ivan'
# print(names)  # !!!!! переменной names не существует
# # NameError: name 'names' is not defined. Did you mean: 'name'?

# # 7. ValueError (Ошибка значения)
# text = 'Python'
# print(int(text))  # !!!!! нельзя символы перевести в целые значения
# # ValueError: invalid literal for int() with base 10: 'Python'
