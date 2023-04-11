

class Human:
    sub_class = 'Человек'

    def __init__(self, name: str, age: int, weight: float = 100, height: float = 170):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def hello(self):
        return f'Тебя приветствует {self.name}'


kirill = Human('Стоун', 38, height=210)
sveta = Human('Света', 18)
kirill.name = 'Стоун'
print(kirill.name)
print(kirill.height)
print(sveta.name)
print(sveta.height)
print(kirill.hello())
print(sveta.hello())
