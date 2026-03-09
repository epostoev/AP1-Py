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


class Car:
    def calculate_travel_time(self, distance):
        return distance // 60

class Bicycle:
    def calculate_travel_time(self, distance):
        return distance // 15


car = Car()
bicycle = Bicycle()

# вызови метод calculate_travel_time() для каждого экземпляра, 
# передав в качестве параметра расстояние
print(car.calculate_travel_time(120))
print(bicycle.calculate_travel_time(45))