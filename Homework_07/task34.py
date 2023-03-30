# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                         Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам        Парам пам-пам

rhymes = 'пара-ра-рам рам-пам-папам па-ра-па-дам'


# Версия 2 (list comprehension and lambda map)
def is_there_a_rhyme(winnie_string):
    phrase_to_vowels_list = [[symb for symb in phrase if symb in 'аеёиоуыэюя'] for phrase in (winnie_string.split())]
    return 'Парам пам-пам' if len(set(map(lambda count: len(count), phrase_to_vowels_list))) == 1 else 'Пам парам'


print(is_there_a_rhyme(rhymes))


# # Версия 1 (brute-force)
# def is_there_a_rhyme(in_string):
#     if not in_string:
#         return 'Пам парам'
#     vowels = 'аеёиоуыэюя'
#     vowels_count_dict = dict()
#     result_list = list()
#     for phrase in in_string.split():
#         for letter in phrase:
#             if letter in vowels:
#                 vowels_count_dict[phrase] = vowels_count_dict.get(phrase, 0) + 1
#     for val in vowels_count_dict.values():
#         result_list.append(val)
#     if len(set(result_list)) == 1:
#         return 'Парам пам-пам'
#     else:
#         return 'Пам парам'
