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

import sys

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # напиши здесь геттер для __salary
    def get_salary(self):
        return self.__salary

    # напиши здесь сеттер для __salary
    def set_salary(self, salary):
        print(id(self))  # выводим id объекта, для которого вызывается метод
        if salary < 0:
            print("Зарплата не может быть отрицательной")
        else:
            self.__salary = salary

employee = Employee('Кот', 10)
print(id(employee))  # выводим id объекта employee

print(employee.get_salary())  # Вывод: 10 рыбов
employee.set_salary(20)
print(employee.get_salary())  # Вывод: 20 рыбов
            