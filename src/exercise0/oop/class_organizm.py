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

class Tester:
    def __init__(self, name):
        self.name = name

    def test(self):
        return f"Тестировщик {self.name} проводит тестирование"
class Autotester(Tester):
    def __init__(self, name, tool): # self = qa_autotester tool = PyTest
        super().__init__(name) # self = qa_autotester, self.name = Шульганташ
        self.tool = tool
    def test(self):
        return f"Автотестировщик {self.name} проводит тестирование c помощью {self.tool}"
qa_tester = Tester("Иван")
qa_autotester = Autotester("Маша", "Selenium")
print(qa_tester.test())
print(qa_autotester.test())
