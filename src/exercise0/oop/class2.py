class Button:
    width = 200 # задай переменные width и height
    height = 50
    def __init__(self, color, text): # допиши метод __init__
        self.button_color = color
        self.button_text = text

# создай объект с цветом кнопки 'жёлтый' и надписью 'Купить'
button_1 = Button("желтый", "Купить") 
# создай объект с цветом кнопки 'красный' и надписью 'Удалить'
button_2 = Button("красный", "Удалить")

print(button_1.width) # выведи ширину жёлтой кнопки
print(button_1.button_color) # выведи цвет жёлтой кнопки
print(button_2.width) # выведи ширину красной кнопки
print(button_2.button_color) # выведи цвет красной кнопки