""" Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
    отломить k долек, если разрешается сделать один разлом по прямой между дольками
    (то есть разломить шоколадку на два прямоугольника).
    Примеры: 1) 3 2 4 -> yes    2) 3 2 1 -> no  """

n = int(input('Введите размер шоколадки, сколько долек в длину: '))
m = int(input('Введите размер шоколадки, сколько долек в ширину: '))
k = int(input('Сколько долек попробуем отломить: '))

if m > n:
    tmp = m
    m = n
    n = tmp

if n == m and k % n == 0:
    print(f'{k} дольки(ек) сможем отломить по любой из сторон шоколадки.')
    print(f'{n} {m} {k} -> yes')
elif k % n == 0:
    print(f'{k} дольки(ек) сможем отломить по длинной стороне шоколадки.')
    print(f'{n} {m} {k} -> yes')
elif k % m == 0:
    print(f'{k} дольки(ек) сможем отломить по короткой стороне шоколадки.')
    print(f'{n} {m} {k} -> yes')
else:
    print(f'От шоколадки размером {n} на {m} долек не сможем отломить {k} дольки(ек).')
    print(f'{n} {m} {k} -> no')
