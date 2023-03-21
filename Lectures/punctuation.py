import string

#  punctuation - multi replace
my_string = 'Мыла_мама/раму.Мама*мыла-Раму'
print(my_string)

# print(string.punctuation)  # выводит: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# вариант цикла for в одну строку
# [my_string.replace(char, ' ') for char in string.punctuation]

for char in string.punctuation:
    my_string = my_string.replace(char, ' ')
print(my_string)
