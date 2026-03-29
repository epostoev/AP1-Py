#!/usr/local/bin/python3
# class Parent:
#     def __init__(self):
#         self._parent_attr = 10

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__child_attr = 20

# child = Child()
# print(child._parent_attr)
# print(child.__child_attr)



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     def print_salary(self):
#         print(f'Зарплата сотрудника "{self.name}" - {self.__salary}')


# employee = Employee('Кот', '10 рыбов')
# employee.print_salary()



# class Car:
#     def __init__(self):
#         self.__fuel = 0            # сделали атрибуты приватными
#         self.__speed = 0

#     def add_fuel(self, amount):    # добавили метод, который заливает топливо
#         if amount > 0:             
#             self.__fuel += amount  

#     def set_speed(self, speed):    # добавили метод, который устанавливает скорость
#         if 0 <= speed <= 120:      
#             self.__speed = speed
#         else:
#             print("Скорость должна быть в пределах от 0 до 120.") 

# # создали объект
# my_car = Car()

# # залили бензин
# my_car.add_fuel(50)       
       
# # разогнали машину 
# my_car.set_speed(90)               
# my_car.set_speed(180)              # Скорость должна быть в пределах от 0 до 120.







# class RobotVacuum:
#     def __init__(self, state):
#         self.__state = state      # атрибут состояния

#     # геттер для получения состояния робота-пылесоса
#     def get_state(self):
#         return self.__state

#     def set_attribute(self, attribute):
#         self.__attribute = attribute
        



# class Car:
#     def __init__(self):
#         self.__fuel = 0  
#         self.__speed = 0

#     def set_speed(self, speed):    # сеттер
#         print(id(self))              # выводим id объекта, для которого вызывается метод
#         if 0 <= speed <= 120:      # скорость может быть от 0 до 120 км/ч
#             self.__speed = speed   
#         else:                      # иначе
#             print("Скорость должна быть в пределах от 0 до 120.")

# my_car = Car()
# my_car_1 = Car()
# print(id(my_car))
# print(id(my_car_1))
# my_car.set_speed(121)
# my_car_1.set_speed(121)


# import sys
# class RobotVacuum:
#     def __init__(self, state):
#         # print(id(self))  # выводим id объекта, для которого вызывается конструктор
#         self.__state = state

#     # геттер получает состояние робота-пылесоса
#     def get_state(self):
#         return self.__state

#     # сеттер устанавливает состояние робота-пылесоса
#     def set_state(self, state):
#         if state in ["работает", "заряжается", "в ожидании"]:
#             self.__state = state
#         else:
#             print(f"Недопустимое состояние: {state}. Состояние может быть 'работает', 'заряжается' или 'в ожидании'")

# # создали объект
# input()
# robo_vacuum = RobotVacuum("в ожидании")

# input()
# # вызвали геттер, чтобы получить состояние робота-пылесоса
# print(robo_vacuum.get_state())  # Вывод: в ожидании

# input()
# # вызвали сеттер, чтобы поменять состояние робота-пылесоса
# robo_vacuum.set_state("работает")
# print(robo_vacuum.get_state())  # Вывод: работает

# input()
# # попытались использовать сеттер, чтобы установить недопустимое состояние
# robo_vacuum.set_state("летает")  # Вывод: Недопустимое состояние: летает. Состояние может быть 'работает', 'заряжается' или 'в ожидании'
# print(robo_vacuum.get_state())   # Вывод: работает 


# v1 = RobotVacuum("work")
# v2 = RobotVacuum("work")
# print(id(v1))
# print(sys.getsizeof(v1))
# print(sys.getsizeof(v2))

# import sys


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []

#     def add_grade(self, grade):
#         if 1 <= grade <= 5:
#             self.grades.append(grade)
#         else:
#             print("Оценка должна быть между 1 и 5")

#     def get_grades(self):
#             print(id(self))  # выводим id объекта, для которого вызывается метод
#             return self.grades
#         # добавь геттер


# student = Student('Двоечкин')

# student.add_grade(2)
# student.add_grade(2)
# student.add_grade(2)
# print(student.get_grades())

# import sys

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     # напиши здесь геттер для __salary
#     def get_salary(self):
#         return self.__salary

#     # напиши здесь сеттер для __salary
#     def set_salary(self, salary):
#         print(id(self))  # выводим id объекта, для которого вызывается метод
#         if salary < 0:
#             print("Зарплата не может быть отрицательной")
#         else:
#             self.__salary = salary

# employee = Employee('Кот', 10)
# print(id(employee))  # выводим id объекта employee

# print(employee.get_salary())  # Вывод: 10 рыбов
# employee.set_salary(20)
# print(employee.get_salary())  # Вывод: 20 рыбов
            

# class RobotVacuum:
#     def __init__(self, state):
#         self.__state = state    # атрибут стал свойством

#     @property                   # теперь это — геттер свойства
#     def state(self):   
#         return self.__state     

# robot = RobotVacuum("В ожидании")

# print(robot.state)



# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius

#     # создай геттер для свойства radius
#     @property
#     def radius(self):
#         return self.__radius

# circle = Circle(5)
# print(circle.radius)  # вызови геттер у объекта circle для свойства radius



# @state.setter # сеттер для свойства state
# def state(self, state):
#     if state in ["работает", "заряжается", "в ожидании"]:
#         self.__state = state
#     else:
#         print(f"Недопустимое состояние: {state}. Состояние может быть 'работает', 'заряжается' или 'в ожидании'") 




# class RobotVacuum:
#     def __init__(self, state):
#         self.__state = state

#     @property                   # геттер для свойства state
#     def state(self):
#         return self.__state

#     @state.setter              # сеттер для свойства state
#     def state(self, state):
#         if state in ["работает", "заряжается", "в ожидании"]:
#             self.__state = state
#         else:
#             print(f"Недопустимое состояние: {state}. Состояние может быть 'работает', 'заряжается' или 'в ожидании'")

# # создали объект
# robo_vacuum = RobotVacuum("в ожидании")

# # обратились к свойству, чтобы получить состояния
# print(robo_vacuum.state)  # Вывод: в ожидании

# # перезаписали свойство, чтобы установить состояние
# robo_vacuum.state = "работает"
# print(robo_vacuum.state)  # Вывод: работает

# # попытались использовать свойство, чтобы установить недопустимое состояние
# robo_vacuum.state = "летает"  # Вывод: Недопустимое состояние: летает. Состояние может быть 'работает', 'заряжается' или 'в ожидании'
# print(robo_vacuum.state)   # Вывод: работает 


# class EBook:
#     def __init__(self, content):
#         self.__content = content
#         self.__current_page = 0

#     @property
#     def content(self):
#         return self.__content
    
#     @content.setter
#     def content(self, new_content):

#         self.__content = new_content

#     @property
#     def current_page(self):
#         return self.__current_page

#     @current_page.setter
#     def current_page(self, current_page):
#         print(f"self.__content = {len(self.__content)}")
#         if current_page < 0:
#             self.__current_page = 0
#         elif current_page >= len(self.__content):
#             self.__current_page = len(self.__content) - 1
#         else:
#             self.__current_page = current_page
#         return self.__current_page

# book_1 = EBook(["Страница_1", "Страница_2", "Страница_3"])

# book_1.content = ["Страница_4", "Страница_5", "Страница_6"]

# print(book_1.content)

# print(book_1.current_page)

# book_1.current_page = 5

# print(book_1.current_page)

# book_1.current_page = 1

# print(book_1.current_page)

# class Product:
#     def __init__(self, name, quantity, price):
#         self.__name = name
#         self.__quantity = quantity
#         self.__price = price
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def quantity(self):
#         return self.__quantity
#     @property
#     def price(self):
#         return self.__price

# kefir = Product("Кефир", 12, 100)

# print(kefir.price)


class Product:
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    @property
    def name(self):
        return self.__name

    # напиши сеттер для свойства name
    @name.setter
    def name(self, new_name):
        self.__name=new_name

    @property
    def quantity(self):
        return self.__quantity

    # напиши сеттер для свойства quantity
    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    @property
    def price(self):
        return self.__price

    # напиши сеттер для свойства price
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            print("Цена не может быть отрицательной")
        else:
            self.__price = new_price


# тут программа создаст объект, вызовет сеттеры и выведет результат
product = Product("Яблоки", 0.6, 120)
product.name = "Апельсины"
product.quantity = 1.2
product.price = 240
print(product.name)
print(product.quantity)
print(product.price)