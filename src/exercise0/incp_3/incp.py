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







class RobotVacuum:
    def __init__(self, state):
        self.__state = state      # атрибут состояния

    # геттер для получения состояния робота-пылесоса
    def get_state(self):
        return self.__state

    def set_attribute(self, attribute):
        self.__attribute = attribute