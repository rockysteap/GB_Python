# В сферу применения рассматриваемых операторов входит:
# 1. Операторы * и **: передача аргументов в функцию.
# 2. Операторы * и **: захват аргументов, переданных в функцию.
# 3. Оператор *: принятие аргументов, содержащих только ключевые слова.
# 4. Оператор *: захват элементов во время распаковки кортежа (tuple).
# 5. Оператор *: распаковка итерируемых объектов в списке или кортеже.
# 6. Оператор **: + распаковка словарей в других словарях.

from random import randint
# Распаковка с помощью * и **

numbers = [2, 1, 3, 4, 7]
more_numbers = [*numbers, 11, 18]
print(*more_numbers, sep=', ')  # 2, 1, 3, 4, 7, 11, 18


fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(fruits[0], fruits[1], fruits[2], fruits[3])  # lemon pear watermelon tomato
print(*fruits)  # lemon pear watermelon tomato


print(*[[1, 4, 7], [2, 5, 8], [3, 6, 9]])  # [1, 4, 7] [2, 5, 8] [3, 6, 9] - 3 separate lists
print(list(zip(*[[1, 4, 7], [2, 5, 8], [3, 6, 9]])))  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


date_info = {'year': "2020", 'month': "01", 'day': "01"}
filename = "{year}-{month}-{day}.txt".format(**date_info)
print(filename)  # 2020-01-01.txt


fruits = ['lemon', 'pear', 'watermelon', 'tomato']
numbers = [2, 1, 3, 4, 7]
print(*numbers, *fruits)  # 2 1 3 4 7 lemon pear watermelon tomato


date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info, **track_info,)
print(filename)  # 2020-01-01-Beethoven-Symphony No 5.txt


# Запаковка с помощью * и **
# Такое использование оператора при упаковке аргументов позволяет создавать свои функции,
# которые (аналогично print и zip) принимают любое количество аргументов.


def roll(*dice):
    return sum(randint(1, die) for die in dice)


print(roll(20))
print(roll(6, 6))
print(roll(6, 6, 6))


# ** захватывает в словарь аргументы ключевых слов, которые мы передаем данной функции.
# Впоследствии аргументы атрибутов (attributes) данной функции смогут на него ссылаться.
def tag(tag_name, **attributes):
    attribute_list = [f'{name}="{value}"'for name, value in attributes.items()]
    return f"<{tag_name} {' '.join(attribute_list)}>"


print(tag('a', href="http://treyhunner.com"))  # <a href="http://treyhunner.com">
print(tag('img', height=20, width=40, src="/face.jpg"))  # <img height="20" width="40" src="/face.jpg">


def get_multiple(*keys, dictionary, default=None):
    return [dictionary.get(key, default) for key in keys]


fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}
print(get_multiple('lemon', 'tomato', 'squash', dictionary=fruits, default='unknown'))  #
# ['yellow', 'red', 'unknown']


def with_previous(iterable, *, fillvalue=None):
    """Yield each iterable item along with the item before it."""
    previous = fillvalue
    for item in iterable:
        yield previous, item
        previous = item


print(list(with_previous([2, 1, 3], fillvalue=0)))  # [(0, 2), (2, 1), (1, 3)]


# Группировка элементов с помощью *

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
first, second, *remaining = fruits
print(remaining)  # ['watermelon', 'tomato']
first, *remaining = fruits
remaining  # ['pear', 'watermelon', 'tomato']
first, *middle, last = fruits
print(middle)  # ['pear', 'watermelon']


fruits = ['lemon', 'pear', 'watermelon', 'tomato']
((first_letter, *remaining), *other_fruits) = fruits
print(remaining)  # ['e', 'm', 'o', 'n']
print(other_fruits)  # ['pear', 'watermelon', 'tomato']


def palindromify(sequence):
    return [*sequence, *reversed(sequence)]


def rotate_first_item(sequence):
    return [*sequence[1:], sequence[0]]


fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print((*fruits[1:], fruits[0]))  # ('pear', 'watermelon', 'tomato', 'lemon')
uppercase_fruits = (f.upper() for f in fruits)
print({*fruits, *uppercase_fruits})  #
# {'lemon', 'watermelon', 'TOMATO', 'LEMON', 'PEAR', 'WATERMELON', 'tomato', 'pear'}


# Оператор ** в литерале словаря


date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
all_info = {**date_info, **track_info}
print(all_info)  # {'year': '2020', 'month': '01', 'day': '01', 'artist': 'Beethoven', 'title': 'Symphony No 5'}


date_info = {'year': '2020', 'month': '01', 'day': '7'}
event_info = {**date_info, 'group': "Python Meetup"}
print(event_info)  # {'year': '2020', 'month': '01', 'day': '7', 'group': 'Python Meetup'}


event_info = {'year': '2020', 'month': '01', 'day': '7', 'group': 'Python Meetup'}
new_info = {**event_info, 'day': "14"}
print(new_info)  # {'year': '2020', 'month': '01', 'day': '14', 'group': 'Python Meetup'}


