# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#            Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#            Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
#            Помогите Кате отгадать задуманные Петей числа.

#       сумма                           произведение
#       x + y = S                       x * y = P
#       x = S - y   подстановка =>      (S - y) * y - P = 0
#                   квадр. ур-е =>      Sy - y^2 - P = 0
#       Дискриминант:                   y^2 - Sy - P = 0
#       D = b^2 - 4ac
#       D = (-S)^2 - 4*1*P              S -> summ, P -> prod

summ = int(input('Введите сумму чисел x и у: '))
prod = int(input('Введите произведение чисел x и y: '))

discriminant = summ ** 2 - 4 * prod
x = (summ + discriminant ** 0.5) / 2
y = (summ - discriminant ** 0.5) / 2

if x.is_integer():
    if discriminant == 0:
        print(f'Петя два раза загадал {int(x)}.')
    elif discriminant > 0:
        print(f'Петя загадал {int(x)} и {int(y)}.')
else:
    print('Некорректный ввод!')
