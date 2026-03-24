# class Robot:
#     def __init__(self, name, energy_level):
#         self.name = name
#         self.energy_level = energy_level

#     def say_hello(self):
#         if self.energy_level > 0:            # проверяем уровень заряда робота
#             self.energy_level -= 10          # если он больше нуля, вычитаем десять единиц
#             return f"Привет, я {self.name}!" # и выводим приветствие
#         else:
#             return "Энергия закончилась :("  # если меньше нуля — выводим предупреждение


# rob_1 = Robot("R2D2", -5)

# print(rob_1.__dict__)

# print(rob_1.say_hello())






# class Car:
#     def __init__(self, speed_limit):
#         self._speed_limit = speed_limit    # защищённый атрибут суперкласса

#     def drive(self, speed):
#         if speed <= self._speed_limit:     
#             print(f"Скорость - {speed} км/ч")
#         else:
#             self._speed_warning()

#     def _speed_warning(self):               # защищённый метод суперкласса
#         print("Слишком высокая скорость!")

# class SportsCar(Car):
#     def __init__(self, speed_limit, turbo_speed):
#         super().__init__(speed_limit)      # подкласс унаследовал защищённый атрибут
#         self._turbo_speed = turbo_speed    # и у него есть свой такой же

#     def turbo_drive(self, speed):          
#         if speed <= self._turbo_speed:
#             print(f"Скорость — {speed} км/ч в турборежиме")
#         else:
#             self._speed_warning()          # защищённый метод тоже унаследован

# my_car = SportsCar(200, 300)
# my_car.turbo_drive(250)  # Скорость — 250 км/ч в турборежиме
# my_car.turbo_drive(350)  # Слишком высокая скорость! 



# class BankAccount:
#     def __init__(self):
#         self.__balance = 0                

#     def deposit(self, amount):            # пополнить счёт
#         if amount > 0:               
#             self.__balance += amount  
#             self.__display_balance()   
#         else:
#             self.__invalid_operation()

#     def withdraw(self, amount):           # снять деньги со счёта
#         if 0 < amount <= self.__balance:  
#             self.__balance -= amount
#             self.__display_balance()
#         else:
#             self.__invalid_operation()

#     def __invalid_operation(self):       # вывести сообщение об ошибке
#         print("Некорректная операция")

#     def __display_balance(self):         # вывести, сколько денег на счёте
#         print(f"Текущий баланс: {self.__balance}")

# # создали объект
# my_account = BankAccount()
# my_account.deposit(200)   # Текущий баланс: 200
# my_account.withdraw(100)  # Текущий баланс: 100 


class Parent:
    def __init__(self):
        self._parent_attr = 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__child_attr = 20

child = Child()

print(child._parent_attr)
# print(child.__child_attr)