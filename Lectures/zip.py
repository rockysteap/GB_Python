users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]

# zip собирает соответствующие элементы коллекций, 1 с 1, 2 с 2 и тд

data = list(zip(users, ids))
print(data)  # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# zip итерирует по коллекции меньшей размерности

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)  # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]
