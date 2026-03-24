
# class Dog():
#     tail = 1 # переменная класса
#     paws = 4 # переменная класса

#     def __init__(self, name, color):
#         self.dog_name = name # атрибут класса
#         self.dog_color = color # атрибут класса 

# from datetime import date

# class Dog:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         input(f"\nPlese press Enter{cls}\n")
#         current_year = date.today().year
#         return cls(name, current_year - birth_year)

# # создали объект класса с годом рождения вместо возраста
# dog = Dog.from_birth_year('Рекс', 2015) # вызываем метод класса
# print(dog.age) # 8 



# import random


# class Cat:

#     def __init__(self, name):
#         self.name = name
#         self.head = 1
#         self.tail = 1
#         self.paws = 4

#     @classmethod
#     def without_name(cls):
#         sample_names = ['Барсик', 'Снежинка', 'Миса', 'Феликс']
#         return cls(random.choice(sample_names))

# cat = Cat.without_name()
# print(cat.name)


# class MyAnimals:
    
#     all_my_animals = 0
    
#     def __init__(self):
#         MyAnimals.all_my_animals = MyAnimals.all_my_animals + 1
       
#     @classmethod
#     def get_aminals_count(cls):
#         return f'I have {cls.all_my_animals}!'

# # Создаём объекты класса     
# my_cat = MyAnimals()
# # при создании объекта вызвали метод init, он изменил значение переменной на 1
# my_dog = MyAnimals()
# # значение переменной стало 2
# my_bird = MyAnimals()

# # Вызываем classmethod 
# print(MyAnimals.get_aminals_count()) # 3 





# class MyAnimals:
    
#     all_my_animals = 0
    
#     def __init__(self):
#         MyAnimals.all_my_animals = MyAnimals.all_my_animals + 1
       
#     @classmethod
#     def get_aminals_count(cls):
#         return f'I have {cls.all_my_animals}!'

# class Cat(MyAnimals):
    
#     all_my_animals = 0
    
#     pass # заглушка, чтобы не писать методы

# class Dog(MyAnimals):

#     all_my_animals = 0
    
#     pass

# class Bird(MyAnimals):

#     all_my_animals = 0
    
#     pass

# # Создаём объекты класса     
# my_first_cat = Cat()
# my_dog = Dog()
# my_second_cat = Cat()
# my_bird = Bird()
# my_second_bird = Bird()
# my_third_bird = Bird()

# # Вызываем classmethod класса-родителя
# print(MyAnimals.get_aminals_count()) # 6

# # теперь вызовем по очереди тот же метод для классов-наследников
# print(Cat.get_aminals_count()) # 0
# print(Dog.get_aminals_count()) # 0
# print(Bird.get_aminals_count()) # 0 






class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def create_margherita(cls):
        ingredients = ['mozzarella', 'tomatoes']
        return cls(ingredients)
    @classmethod
    def create_hawaiian(cls):
        ingredients = ['mozzarella', 'tomatoes', 'ananas', 'ham']
        return cls(ingredients)

print(Pizza.create_margherita().ingredients) # ['mozzarella', 'tomatoes']
print(Pizza.create_hawaiian().ingredients) # ['mozzarella', 'tomatoes', 'ananas', 'ham']