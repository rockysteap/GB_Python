# Быстрая сортировка (постоянное деление пополам)
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    lesser = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


# print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))
# print(quick_sort([10, 5, 2]))

# Сортировка слиянием (деление пополам до однозначных списков)
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


# my_list = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
# merge_sort(my_list)
# print(my_list)
