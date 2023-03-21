# 1. I like Python
#    Напишите программу, которая выводит на экран текст «I***like***Python» (без кавычек).
#    print("I", "like", "Python", sep="***")

# 2. Управляемый разделитель
#    Напишите программу, которая считывает строку-разделитель и три строки,
#    а затем выводит указанные строки через разделитель.
# a = input()
# b = input()
# c = input()
# d = input()
# print(b, c, d, sep=a)

# 3. Сумма трёх чисел
#    Напишите программу, которая считывает три целых числа и выводит на экран их сумму.
#    Каждое число записано в отдельной строке.
# a = int(input())
# a += int(input())
# a += int(input())
# print(a)

# 4. Следующее и предыдущее
#    Напишите программу, которая считывает целое число, после чего на экран выводится следующее и
#    предыдущее целое число с пояснительным текстом.
# a = int(input())
# print(f'Предыдущее число -> {a - 1}')
# print(f'Следующее число -> {a + 1}')

# 5. Разделяй и властвуй
#    Напишите программу, которая считывает целое положительное число xx и выводит на экран
#    последовательность чисел x, 2x, 3x, 4x, 5x, разделённых тремя черточками.
# x = int(input())
# print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep="-" * 3)

# 6. Расстояние в метрах
#    Напишите программу, которая находит полное число метров по заданному числу сантиметров.
# cm = int(input())
# print(f'{cm}см это {cm // 100}м {cm % 100}см')

# 7. Сама неотвратимость
#    Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения
#    Вселенной по щелчку пальцев. При этом если население Вселенной является нечетным числом,
#    то титан проявит милосердие и округлит количество выживших в большую сторону.
#    Помогите Мстителям подсчитать количество выживших.
# a = int(input())
# print(a // 2 + a % 2)

# 8. Пересчет временного интервала
#    Напишите программу для пересчёта величины временного интервала, заданного в минутах,
#    в величину, выраженную в часах и минутах.
# m = int(input())
# print(f'{m} мин это {m // 60} ч {m % 60} мин')

# 9. Трехзначное число
#    Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# n = int(input())
# способ 1:
# a = n % 10
# b = n // 10 % 10
# c = n // 100
# способ 2:
# n = (input())
# a = int(n[0])
# b = int(n[1])
# c = int(n[2])
# print(f'Цифры {a},{b},{c} -> сумма = {a+b+c}, произведение = {a*b*c}.')

# 10. Четырёхзначное число
#     Напишите программу для нахождения цифр четырёхзначного числа.
# n = int(input())
# a = n % 10
# b = n // 10 % 10
# c = n // 100 % 10
# d = n // 1000
# print(f'Цифры -> {a},{b},{c},{d}')

# 11. Пароль
#     При регистрации на сайтах требуется вводить пароль дважды.
#     Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

#     Напишите программу, которая сравнивает пароль и его подтверждение.
#     Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
# a = input()
# b = input()
# print('Пароль принят') if a == b else print('Пароль не принят')

# 12. Четное или нечетное?
#     Напишите программу, которая определяет, является число четным или нечетным.
# a = int(input())
# 1 способ:
# print('Четное!') if a % 2 == 0 else print('Нечетное!')
# 2 способ:
# print('Нечетное!') if a % 2 else print('Четное!')

# 13. Роскомнадзор
#     Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
#     На вход программе подаётся целое число — возраст пользователя.
#     Программа должна вывести текст «Доступ разрешен» если возраст не менее 18,
#     и «Доступ запрещен» в противном случае.
# age = int(input('Укажите ваш возраст: '))
# print('Доступ запрещен') if age < 18 else print('Доступ разрешен')

# 14. Арифметическая прогрессия
#     Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке)
#     последовательными членами арифметической прогрессии.
# num3 = int(input())
# num2 = int(input())
# num1 = int(input())
# print('Является') if num3 - num2 == num2 - num1 else print('Не является')

# 15. Наименьшее из четырёх чисел
#     Напишите программу, которая определяет наименьшее из четырёх чисел.
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# 1 способ:
# if a > b:    a = b
# if c > d:    c = d
# if a > c:    a = c
# print(a)
# 2 способ:
# print(min(a, b, c, d))

# 16. Только положительные
#     Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
# num_list = list()
# sum = 0
# for i in range(3):
#     num_list.append(int(input()))
# for i in range(len(num_list)):
#     if num_list[i] > 0:
#         sum += num_list[i]
# print(sum)

# n = int(input('Введите число: '))
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1