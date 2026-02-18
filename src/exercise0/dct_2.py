neighbours =  {
    11 : ['Александр', 'Света'],
    21 : ['Лиза', 'Артём'],
    26 : ['Антон', 'Надя'],
    9 : ['Евгений', 'Маша'],
    5 : ['Катя', 'Костя'],
    33 : ['Сергей', 'Инга']
}

# твой код здесь
replace_symbol = ['[', ']', '\'']


for key, value in neighbours.items():
    value_str = str(value)
    value_str = value_str.replace('[', "")
    value_str = value_str.replace(']', "")
    value_str = value_str.replace('\'', "")
    print(value_str + " живут в квартире " + str(key))