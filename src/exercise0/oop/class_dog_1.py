class Dog():
    tail = 1 # переменные класса одинаковые у всех объектов
    paws = 4

    def __init__(self, name, color): # метод __init__, задаёт имя и цвет
        self.dog_name = name
        self.dog_color = color

    def bark(self): # метод, с помощью которого собака гавкает
        print('гав-гав')

class DogOwner():
    def __init__(self, name, cat):
        self.name = name
        self.my_dog = cat

    def ask_dog_to_bark(self): # метод просит собачку погавкать
        self.my_dog.bark()

    def say_dogs_color(self): # метод называет цвет собачки
        print('У меня собака цвета', self.my_dog.dog_color)

    def call_dog_by_name(self): # метод зовёт собачку по имени
        # Напиши свой код здесь
        print("Ко мне," + self.my_dog.dog_name)
    
dog_1 = Dog("Барбос", "Черной-Белый")
human_1 = DogOwner("Сергей", dog_1)

print(human_1.name)
human_1.call_dog_by_name()
human_1.say_dogs_color()