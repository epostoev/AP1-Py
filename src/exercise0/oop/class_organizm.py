# ... создай три класса: ElectronicDevice, Television и Computer
class ElectronicDevice:
    def power_on(self):
        print(f"Устройство включено")
    def power_off(self):
        print(f"Устройство выключено")

class Television(ElectronicDevice):
    def change_channel(self):
        print(f"Канал был изменен")
class Computer(ElectronicDevice):
    def open_application(self):
        print(f"Приложение было открыто")


electronic_device = ElectronicDevice()
# ... вызови методы power_on() и power_off() для объекта electronic_device
electronic_device.power_off()
electronic_device.power_on()

television = Television()
# ... вызови методы power_on(), power_off() и change_channel() для объекта television
television.power_on()
television.power_off()
television.change_channel()

computer = Computer()
# ... вызови методы power_on(), power_off() и open_application() для объекта computer
computer.power_on()
computer.power_off()
computer.open_application()
##############################################

# суперкласс
class StringInstrument:
    def __init__(self, name, number_of_strings):
        self.name = name
        self.number_of_strings = number_of_strings

    def play(self):
        return f"Играем на инструменте {self.name}"

    def tune(self):
        return f"Настраиваем инструмент {self.name}. Количество струн: {self.number_of_strings}"

# подкласс Guitar
class Guitar(StringInstrument):               
    def __init__(self, number_of_strings):
        # self.name = 'Гитара'
        StringInstrument.__init__(self, 'Гитарка', number_of_strings) #вызов конструктора
 
    def play_chords(self):
        return f"Играем аккорды на инструменте {self.name}" 

 
gitar_1 = Guitar(3)

print(gitar_1.play_chords())