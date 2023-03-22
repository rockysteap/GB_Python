# import module
# from module import max1
# from module import *
# import module as m

# print(module.max1(5, 9))
# print(max1(5, 9))
# print(m.max1(5, 9))

from sorting import *

print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))
print(quick_sort([10, 5, 2]))

my_list = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(my_list)
print(my_list)
