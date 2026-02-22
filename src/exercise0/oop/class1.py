class Dog():
    tail = 1
    paws = 4
    def __init__(self, name, color):
        self.dog_name = name
        self.dog_color = color
    def kitap(self):
        print("Гав гав - меня зовут ", self.dog_name)

dog1 = Dog("Шарик", "Белый")
dog2 = Dog("Тузик", "Серый")
dog3 = Dog("Мухтар", "Черный")

print(dog1.dog_name)
dog1.kitap()
print(dog2.dog_name)
print(dog3.dog_name)

