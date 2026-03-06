class Dog():  
    tail = 1 # переменные класса одинаковые у всех объектов
    paws = 4

    def __init__(self, name, color): # метод __init__, задаёт имя и цвет
        self.dog_name = name
        self.dog_color = color

    def bark(self):  # метод, с помощью которого собака гавкает
        print('гав-гав')  

dog1 = Dog("Шарик", "Red")

# print(dog1.tail)
# print(dog1.dog_name)

class Human():
    def __init__(self,name): # у человека есть имя
        self.name = name

    def adopt_dog(self, dog): # метод заводит собачку
        print('У меня есть собачка')
        self.my_dog = dog # добавили собачку как атрибут человеку
    def ask_dog_to_bark(self):
        self.my_dog.bark()


human_1 = Human("Саша")
dog_1 = Dog("Шульган", "Черный")

human_1.adopt_dog(dog_1)
human_1.ask_dog_to_bark()