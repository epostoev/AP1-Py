class MyDog():

    name = 'Барбос'
    mood = 50
    satiety = 50

    def give_dog_food(self):
        self.satiety += 10
        print(self.name, 'сыт на', self.satiety, 'процентов!')

    def pet_dog(self):
        # пиши код здесь 
        self.mood +=25
        print(self.name, 'доволен на', self.mood, 'процентов!')


dog_1 = MyDog()
dog_1.pet_dog()