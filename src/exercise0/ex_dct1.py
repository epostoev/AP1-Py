new_neighbours = [['Вася', 'Катя'], ['Юра', 'Марина'], ['Лёша', 'Ира'], ['Петя', 'Надя'], ['Ваня', 'Света']]

house_dict = {}

for i in range(0,len(new_neighbours)):
# твой код
    house_dict[i + 1] = new_neighbours[i]
print(house_dict)