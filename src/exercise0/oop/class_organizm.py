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