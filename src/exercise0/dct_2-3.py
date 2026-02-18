neighbours =  {
    11 : ['Александр', 'Света'],
    21 : ['Лиза', 'Артём'],
    26 : ['Антон', 'Надя'],
    9 : ['Евгений', 'Маша'],
    5 : ['Катя', 'Костя'],
    33 : ['Сергей', 'Инга']
}

# Выведи на экран, сколько людей живёт в квартире 11 (число)
print(len(neighbours[11]))

# Выведи на экран построчно всех жильцов квартиры 21
for key, value in neighbours.items():
    if key == 21:
        for i in range(len(value)):
            print(value[i])

# Выведи на экран имена всех вторых жильцов
for key, value in neighbours.items():
    print(value[1])
