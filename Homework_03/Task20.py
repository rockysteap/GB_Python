# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#               В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
#               D, G – 2 очка; B, C, M, P – 3 очка;
#               F, H, V, W, Y – 4 очка;
#               K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
#               А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#               Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
#               Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
#               Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#               Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
#               либо только русские буквы.
#               Пример:  ноутбук  #  12

import scrabble
# scramble.py (в той же папке)
# is_en_alphabet(word), is_ru_alphabet(word) - проверяет относится ли слово к одному из языков
# en_score(word), ru_score(word) - считает очки для двух языков

print('Welcome to Scrabble! Enter a word in Eng or Rus.')
print('Добро пожаловать в Эрудит! Введите слово на русском или английском.')
user_input = input('-> ')
score = 0

if scrabble.is_en_alphabet(user_input):
    score = scrabble.en_score(user_input)
    print(f'The word \'{user_input}\' scored with {score} points.')
elif scrabble.is_ru_alphabet(user_input):
    score = scrabble.ru_score(user_input)
    print(f'Слово \'{user_input}\' набрало {score} балла(ов).')
else:
    print('Ошибка: некорректный ввод.')


# Проверка алфавита с использованием ord():
# ord() возвращает Unicode из заданного символа
# (иными словами, принимает строку единичной длины в качестве аргумента
# и возвращает эквивалентность Юникода переданного аргумента)
# 65 - 122 -> unicodes английского алфавита от большой 'A' до маленькой 'z'
# 1040 - 1103 -> unicodes русского алфавита 'А' -> 'я'

en_total = scrabble.en_score(user_input)
ru_total = scrabble.ru_score(user_input)
word = user_input

if all(list(map(lambda x: 64 < ord(x) < 123, word))):
    print(f'Английское слово \'{word}\' весит {en_total} баллов.')
elif all(list(map(lambda x: 1039 < ord(x) < 1104, word))):
    print(f'Русское слово \'{word}\' весит {ru_total} баллов.')
else:
    print(f'Слово не соответствует ни английскому, ни русскому алфавиту.')
