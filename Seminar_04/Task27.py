# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
import string

# input_str1 = 'Мама мыла раму мама Мыла Раму'

# input_str = f'Пользователь вводит текст строка.' \
#             f'Словом считается последовательность непробельных символов идущих подряд, ' \
#             f'слова разделены одним или большим числом пробелов или символами конца строки.' \
#             f'Определите, сколько различных слов содержится в этом тексте.'
#
# print(len(set(input_str.replace('.', ' ').lower().split())))

#  punctuation - multi replace
my_string = 'Мыла_мама/раму.Мама*мыла-Раму'

# print(string.punctuation)
# вариант цикла for
# [my_string.replace(char, ' ') for char in string.punctuation]

for char in string.punctuation:
    my_string = my_string.replace(char, ' ')

print(my_string)
my_string = my_string.lower().split()


