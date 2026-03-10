# ... создай три класса: ElectronicDevice, Television и Computer
# class ElectronicDevice:
#     def power_on(self):
#         print(f"Устройство включено")
#     def power_off(self):
#         print(f"Устройство выключено")

# class Television(ElectronicDevice):
#     def change_channel(self):
#         print(f"Канал был изменен")
# class Computer(ElectronicDevice):
#     def open_application(self):
#         print(f"Приложение было открыто")


# electronic_device = ElectronicDevice()
# # ... вызови методы power_on() и power_off() для объекта electronic_device
# electronic_device.power_off()
# electronic_device.power_on()

# television = Television()
# # ... вызови методы power_on(), power_off() и change_channel() для объекта television
# television.power_on()
# television.power_off()
# television.change_channel()

# computer = Computer()
# # ... вызови методы power_on(), power_off() и open_application() для объекта computer
# computer.power_on()
# computer.power_off()
# computer.open_application()

##############################################

# суперкласс
# class StringInstrument:
#     def __init__(self, name, number_of_strings):
#         self.name = name
#         self.number_of_strings = number_of_strings

#     def play(self):
#         return f"Играем на инструменте {self.name}"

#     def tune(self):
#         return f"Настраиваем инструмент {self.name}. Количество струн: {self.number_of_strings}"

# # подкласс Guitar
# class Guitar(StringInstrument):               
#     def __init__(self, number_of_strings):
#         # self.name = 'Гитара'
#         StringInstrument.__init__(self, 'Гитарка', number_of_strings) #вызов конструктора
 
#     def play_chords(self):
#         return f"Играем аккорды на инструменте {self.name}" 

 
# gitar_1 = Guitar(3)

# print(gitar_1.play_chords())


# class Medication:
#     def __init__(self, name, dosage):
#         self.name = name
#         self.dosage = dosage

#     def consume(self):
#         print(f"Принято лекарство - {self.name}. Доза - {self.dosage}")


# class Tablet(Medication):
#     # напиши конструктор, вызови в нём конструктор суперкласса и добавь новый атрибут colour
#     def __init__ (self, name, dosage, colour):
#         Medication.__init__(self, name, dosage)
#         self.colour = colour


#     def print_colour(self):
#         print(f"Цвет таблетки - {self.colour}")


# tablet = Tablet("Наследин", "2", "Белый")
# tablet.consume()       # Принято лекарство - Наследин. Доза - 2
# tablet.print_colour()  # Цвет таблетки - Белый


# class StringInstrument:
#     def __init__(self, name, number_of_strings):
#         self.name = name
#         self.number_of_strings = number_of_strings

 
#     def play(self):
#         return f"Играем на инструменте {self.name}"

#     def tune(self):
#         return f"Настраиваем инструмент {self.name}. Количество струн: {self.number_of_strings}"

# # подкласс Violin
# class Violin(StringInstrument):               
#     def __init__(self, number_of_strings):
#         self.name = 'Скрипка'
#         super().__init__(self.name, number_of_strings) # вызов конструктора суперкласса

# # подкласс Guitar
# class Guitar(StringInstrument):               
#     def __init__(self, number_of_strings):
#         self.name = 'Гитара'
#         super().__init__(self.name, number_of_strings) # вызов конструктора суперкласса

# viola = Violin(4)
# gitar = Guitar(6)
# print(viola.play())
# print(viola.tune())
# print(gitar.play())
# print(gitar.tune())
# print(isinstance(viola, Violin)) 
# print(isinstance(viola, StringInstrument))

######################

# class Tester:
#     def __init__(self, name):
#         self.name = name

#     def test(self):
#         return f"Тестировщик {self.name} проводит тестирование"
# class Autotester(Tester):
#     def __init__(self, name, tool): # self = qa_autotester tool = PyTest
#         super().__init__(name) # self = qa_autotester, self.name = Шульганташ
#         self.tool = tool
#     def test(self):
#         return f"Автотестировщик {self.name} проводит тестирование c помощью {self.tool}"
# qa_tester = Tester("Иван")
# qa_autotester = Autotester("Маша", "Selenium")
# print(qa_tester.test())
# print(qa_autotester.test())


# class Medication:
#     def __init__(self, name, dosage):
#         self.name = name
#         self.dosage = dosage

#     def consume(self):
#         print(f"Принято лекарство - {self.name}. Доза - {self.dosage}")


# class Tablet(Medication):
#     # напиши конструктор, используя super(), вызови в нём конструктор суперкласса
#     # добавь новый атрибут colour
#     def __init__(self, name, dosage, colour): # self = tablet; name = Наследин; dosage = 2; colour = Белый
#         super().__init__(name, dosage)
#         self.colour  = colour

#     def print_colour(self):
#         print(f"Цвет таблетки - {self.colour}")


# class Injection(Medication):
#     # напиши конструктор, используя super(), вызови в нём конструктор суперкласса
#     # добавь новый атрибут needle_length
#     def __init__(self, name, dosage, needle_length):
#         super().__init__(name, dosage)
#         self.needle_length = needle_length

#     def consume(self):
#         print(f"Инъекция {self.name} сделана. Доза - {self.dosage}")

#     def print_needle_length(self):
#         print(f"Длина иглы - {self.needle_length}")


# tablet = Tablet("Наследин", 2, "Белый") 
# tablet.consume()       # Принято лекарство - Наследин. Доза - 2
# tablet.print_colour()  # Цвет таблетки - Белый
# injection = Injection('ООПин', 1, "Средняя")
# injection.consume()     # Инъекция ООПин сделана. Доза - 1
# injection.print_needle_length()  # Длина иглы - Средняя


# class Book:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

#     def read(self, page):
#         return f"Читаем книгу '{self.title}' - {self.content[page]}"

# # тут напиши реализацию подкласса Audiobook
# class Audiobook(Book):
#     def __init__(self, title, content):
#         super().__init__(title, content)
#     def listen(self, page):
#         return f"Воспроизводим страницу {self.content[page]} из аудиокниги {self.title}"



# book = Book("Война и мир", ["Страница 1", "Страница 2", "Страница 3"])
# print(book.read(1))          # Читаем книгу Война и мир - Страница 2

# audiobook = Audiobook("1984", ["Страница 1", "Страница 2"])
# print(audiobook.listen(0))   # Воспроизводим страницу 1 из аудиокниги 1984

# class Artist:
#     def __init__(self):
#         self.art_creation_time = 5  # часов на одну картину

#     def create_art(self, time):
#         return time // self.art_creation_time


# class Sculptor(Artist):
#     def __init__(self):
#         super().__init__()
#         self.stone_needed = 3  # камня на одну скульптуру

#     # переопредели метод create_art()
#     def create_art(self, stone):
#         return stone // self.stone_needed


# painter = Artist()
# print(painter.create_art(20))    # 4 картины

# sculptor = Sculptor()
# print(sculptor.create_art(8))    # 2 скульптуры


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}.")


# class SpiderMan(Person):
#     def __init__(self, name):
#         super().__init__(name)

#     def introduce(self, with_identity=False):
#         # переопредели метод суперкласса, используя super()
#         super().introduce()
#         if with_identity == 1:
#             print(f"Но вы можете знать меня как Человека-паука.")
# 				# добавь новое условие, используя with_identity


# peter = SpiderMan("Питер Паркер")
# peter.introduce(with_identity=True)  
# # Привет, меня зовут Питер Паркер. 
# # Но вы можете знать меня как Человека-паука.



# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         self.balance -= amount

#         return self.balance


# # наследуй класс от BankAccount и переопредели метод withdraw
# class SavingsAccount(BankAccount):
#     def __init__(self, balance, interest_rate):
#         # передам баланс родителю
#         super().__init__(balance)
#         self.interest_rate = interest_rate
#     def withdraw(self, amount):
#         # рассчитываем процент
#         fee = self.interest_rate * amount
#         # Вызываем метод родителя и передам ему сумму
#         self.balance = super().withdraw(amount) - fee

#         return self.balance



# # пример использования
# acc = BankAccount(1000)
# print(acc.withdraw(100))          # вывод: 900

# savings_acc = SavingsAccount(1000, 0.05)
# print(savings_acc.withdraw(100))  # вывод: 895



# создай классы Animal, Dog и Cat, в каждом из которых будет метод make_sound
# class Animal():
#     def __init__(self, energy):
#         self.energy = energy
#     def make_sound(self):
#         self.energy -= 5
#         return self.energy
# class Dog(Animal):
#     def make_sound(self):
#         self.energy -= 10 
#         print(f"Гав")
#         return self.energy
# class Cat(Animal):
#     def make_sound(self):
#         self.energy -= 2
#         print(f"Гав")
#         return self.energy
    

# # пример использования
# animal = Animal(100)
# print(animal.make_sound())  # вывод: 95

# dog = Dog(100)
# print(dog.make_sound())  # вывод: "Гав" 90

# cat = Cat(100)
# print(cat.make_sound())  # вывод: "Мяу" 98


# class Car:
#     def calculate_travel_time(self, distance):
#         return distance // 60

# class Bicycle:
#     def calculate_travel_time(self, distance):
#         return distance // 15


# car = Car()
# bicycle = Bicycle()

# # вызови метод calculate_travel_time() для каждого экземпляра, 
# # передав в качестве параметра расстояние
# print(car.calculate_travel_time(120))
# print(bicycle.calculate_travel_time(45))

# class LandAnimal:
#     def walk(self):
#         print("Ходит")

#     def run(self):
#         print("Бегает")

# class WaterAnimal:
#     def swim(self):
#         print("Плавает")

# class Amphibian(LandAnimal, WaterAnimal):
#     def run(self):
#         print("Этот вид не бегает.")

# frog = Amphibian()
# frog.walk()  # Ходит
# frog.swim()  # Плавает
# frog.run()   # Этот вид не бегает.


# class Animal:
#     distance_travelled = 0
#     calories_consumed = 0

#     def move(self):
#         self.distance_travelled += 5
#         return self.distance_travelled

#     def eat(self):
#         self.calories_consumed += 10
#         return self.calories_consumed


# class Plant:
#     height = 0
#     energy_stored = 0

#     def grow(self):
#         self.height += 1
#         return self.height

#     def photosynthesize(self):
#         self.energy_stored += 10
#         return self.energy_stored


# # добавь класс ZombieHerbivore, который наследуется от Animal и Plant
# class ZombieHerbivore(Animal, Plant):
#     pass

# # вызов методов для объекта класса ZombieHerbivore
# zombie = ZombieHerbivore()
# print(zombie.move())
# print(zombie.eat())
# print(zombie.grow())





# class LandAnimal:
#     def __init__(self):
#         self.can_walk = True

#     def walk(self):
#         if self.can_walk:
#             print("Ходит")
#         else:
#             print("Не может ходить")

# class WaterAnimal:
#     def __init__(self):
#         self.can_swim = True

#     def swim(self):
#         if self.can_swim:
#             print("Плавает")
#         else:
#             print("Не может плавать")

# class Amphibian(LandAnimal, WaterAnimal):
#     def __init__(self):
#         LandAnimal.__init__(self) # вызвали конструктор первого суперкласса
#         WaterAnimal.__init__(self) # вызвали конструктор второго суперкласса

# frog = Amphibian()
# frog.walk()  # Ходит
# frog.swim()  # Плавает


# class Animal:
#     def __init__(self):
#         self.distance_travelled = 0
#         self.calories_consumed = 0

#     def move(self):
#         self.distance_travelled += 5

#     def eat(self):
#         self.calories_consumed += 10


# class Plant:
#     def __init__(self):
#         self.height = 0
#         self.energy_stored = 0

#     def grow(self):
#         self.height += 1

#     def photosynthesize(self):
#         self.energy_stored += 10


# class ZombieHerbivore(Animal, Plant):
#     def __init__(self):
#         Plant.__init__(self)
#         Animal.__init__(self)


# zombie = ZombieHerbivore()
# zombie.grow()    # height теперь будет 1
# zombie.move()    # AttributeError: 'ZombieHerbivore' object has no attribute 'distance_travelled'
# print(zombie.height)  # 1
# print(zombie.distance_travelled)  # 5





# class Warrior:
#     def __init__(self):
#         self.strength = 10
#         self.health = 100

#     def attack(self):
#         attack_power = self.strength * 5
#         print(f"Атакуем с силой {attack_power}!")


# class Mage:
#     def __init__(self):
#         self.magic = 10
#         self.intelligence = 10

#     def cast_spell(self):
#         spell_power = self.magic * self.intelligence
#         print(f"Применяем заклинание силой {spell_power}!")

# # реализуй класс BattleMage с множественным наследованием
# class BattleMage(Warrior, Mage):
#     def __init__(self):
#         Warrior.__init__(self)
#         Mage.__init__(self)


# battleMage = BattleMage()
# battleMage.attack()
# battleMage.cast_spell()


# class Vehicle:
#     def speed(self):
#         return "Скорость транспортного средства не определена"

# class Car(Vehicle):
#     def speed(self):
#         return "Скорость автомобиля 100 км/ч"

# class Plane(Vehicle):
#     def speed(self):
#         return "Скорость самолета 900 км/ч"

# class FlyingCar(Car, Plane):
#     pass

# flying_car = FlyingCar()
# print(flying_car.speed())


# class Animal:
#     def sound(self):
#         return "тихое молчание"


# class Dog(Animal):
#     def sound(self):
#         return "Гав!"


# class Cat(Animal):
#     def sound(self):
#         return "Мяу!"


# class CatDog(Dog, Cat):
#     def __init__(self):
#         Dog.__init__(self)
#         Cat.__init__(self)
#     def sound(self):
#         return Cat.sound(self) + ' ' + Dog.sound(self)



# my_pet = CatDog()
# print(my_pet.sound())
# # TypeError: Cannot create a consistent method resolution
# # order (MRO) for bases Animal, Dog, Cat


# class SleepMixin:

#     def start_sleeping(self):
#         print("Засыпаю...")

#     def stop_sleeping(self):
#         print("Просыпаюсь!")

# class EatMixin:
#     def __init__(self):
#         self.is_eating = False
#         self.food = None

#     def start_eating(self, food):
#         self.is_eating = True
#         self.food = food
#         print(f"Начинаю есть {food}...")

#     def stop_eating(self):
#         self.is_eating = False
#         print("Закончил есть!")

# class Human(SleepMixin, EatMixin):
#     def __init__(self):
#         SleepMixin.__init__(self)
#         EatMixin.__init__(self)

#     def go_to_work(self):
#         print("Иду на работу!")

# bob = Human()
# bob.start_sleeping()  # Засыпаю...
# bob.stop_sleeping()   # Просыпаюсь!
# bob.start_eating("яблоко")  # Начинаю есть яблоко...
# print(bob.is_eating, bob.food)  # True, "яблоко"
# bob.stop_eating()     # Закончил есть!
# print(bob.is_eating)  # False
# bob.go_to_work()      # Иду на работу! 


# место для миксинов
# class BatTransformableMixin():
#     def transform_into_bat(self):
#         return "Превращение в летучую мышь"

# class WolfTransformableMixin():
#     def transform_into_wolf(self):
#         return "Превращение в волка"

# class RunnableMixin():
#     def run(self):
#         return "Беги, Форрест, беги!"


# # наследуется от RunnableMixin
# class Human(RunnableMixin):
#     pass


# # наследуется от BatTransformableMixin и RunnableMixin
# class Vampire(BatTransformableMixin, RunnableMixin):
#     pass


# # наследуется от WolfTransformableMixin
# class Werewolf(WolfTransformableMixin):
#     pass


# human = Human()
# vampire = Vampire()
# werewolf = Werewolf()

# print(human.run())                      
# print(vampire.run())                    
# print(vampire.transform_into_bat())     
# print(werewolf.transform_into_wolf())



# # для класса Species реализуй конструктор и метод grow()
# class Species:
#     def __init__(self, population, growth_rate):
#         self.population = population
#         self.growth_rate = growth_rate

#     def grow(self):
#         self.population += self.population * self.growth_rate
#         return self.population
        


# species = Species(1000, 0.02)
# print(species.population)
# species.grow()
# print(species.population)




# class Species:
#     def __init__(self, population, growth_rate):
#         self.population = population
#         self.growth_rate = growth_rate

#     def grow(self):
#         self.population += self.population * self.growth_rate


# # наследуй класс Predator от Species, реализуй конструктор и метод survive()
# class Predator(Species):
#     def __init__(self, population, growth_rate, hunting_success_rate):
#         super().__init__(population, growth_rate)
#         self.hunting_success_rate = hunting_success_rate

#     def survive(self):
#         self.population -= self.population * (1 - self.hunting_success_rate)
#         return self.population 


# predator = Predator(1000, 0.02, 1.05)
# print(predator.population)
# predator.survive()
# print(predator.population)






# class Species:
#     def __init__(self, population, growth_rate):
#         self.population = population
#         self.growth_rate = growth_rate

#     def grow(self):
#         self.population += self.population * self.growth_rate


# # наследуй класс Herbivore от Species, реализуй конструктор и 
# # переопредели метод grow()
# class Herbivore(Species):
#     def __init__(self, population, growth_rate, food_availability):
#         super().__init__(population, growth_rate)
#         self.food_availability = food_availability

#     def grow(self):
#         if self.food_availability > 0.2:
#             self.population += self.population * self.growth_rate
#             self.food_availability -= 0.15
#         else:
#             self.migrate()
#         return self.population

#     def migrate(self):
#         self.population -= 0.2 * self.population
#         self.food_availability = 0.3


# herbivore = Herbivore(2000, 0.04, 0.3)
# herbivore.grow()
# print(herbivore.population)
# print(herbivore.food_availability)
# herbivore.grow()
# print(herbivore.population)
# print(herbivore.food_availability)




class Species:
    def __init__(self, population, growth_rate):
        self.population = population
        self.growth_rate = growth_rate

    def grow(self):
        self.population += self.population * self.growth_rate


class Predator(Species):
    def __init__(self, population, growth_rate, hunting_success_rate):
				# явный вызов класса Species
        Species.__init__(self, population, growth_rate)  
        self.hunting_success_rate = hunting_success_rate

    def survive(self):
        self.population -= self.population * (1 - self.hunting_success_rate)


class Herbivore(Species):
    def __init__(self, population, growth_rate, food_availability):
				# явный вызов класса Species
        Species.__init__(self, population, growth_rate)
        self.food_availability = food_availability

    def grow(self):
        if self.food_availability > 0.2:
            self.population += self.growth_rate * self.population
            self.food_availability -= 0.15
        else:
            self.migrate()

    def migrate(self):
        self.population -= 0.2 * self.population
        self.food_availability = 0.3


# наследуйся от классов Predator и Herbivore, реализуй конструктор и 
# переопредели метод grow()
class Omnivore(Predator, Herbivore):
    def __init__(self, population, growth_rate, hunting_success_rate, food_availability, diet_balance):
        Predator.__init__(self, population, growth_rate, hunting_success_rate)
        Herbivore.__init__(self, population, growth_rate, food_availability)
        self.diet_balance = diet_balance

    def grow(self):
        if self.diet_balance >= 0.5:
            Predator.survive(self)
        elif self.diet_balance < 0.5:
            Herbivore.grow(self)
        

omnivore_herbivore = Omnivore(1000, 0.05, 1, 0.6, 0.4)
print(omnivore_herbivore.population)
omnivore_herbivore.grow()
print(omnivore_herbivore.population)

omnivore_predator = Omnivore(500, 0.02, 1.2, 0.5, 0.6)
print(omnivore_predator.population)
omnivore_predator.grow()
print(omnivore_predator.population)