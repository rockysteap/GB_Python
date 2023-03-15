# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.

from random import randint

# melons = int(input('Введите кол-во арбузов: '))
melons = 10  # зададим для отладки
first_heavy_melon, second_heavy_melon = 0, 0

for i in range(melons):
    current_melon_weight = randint(500, 30000)  # ягоду легче 500г за арбуз не считаем
    if current_melon_weight > second_heavy_melon:
        second_heavy_melon = current_melon_weight
        if second_heavy_melon > first_heavy_melon:
            first_heavy_melon, second_heavy_melon = second_heavy_melon, first_heavy_melon
print(f'Арбуз для себя любимого {first_heavy_melon/1000:2.3f} кг, ну и для тёщи {second_heavy_melon/1000:2.3f} кг.')
