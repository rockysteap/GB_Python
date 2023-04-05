#  enumerate добавляет итератор к итерируемому объекту

# в следующем примере добавляет нумерацию к элементам списка
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)  # [(0, 'user1'), (1, 'user2'), (2, 'user3))]
