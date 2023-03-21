my_string = '1234567890'
my_string = list(my_string)

# map применяет функцию int() ко всем элементам коллекции
my_string = list(map(int, list(my_string)))
print(sum(my_string))
