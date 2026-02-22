class Portal:
    def __init__(self, name, url): # Допиши нужные аргументы):
        self.name = name
        self.url = url# Допиши атрибут url

    def show_info(self):
        print("Это портал: ", self.name)

kinopoisk = Portal("Kinopoisk", 'https://www.kinopoisk.ru/')# Допиши нужное значение)
print(kinopoisk.url)