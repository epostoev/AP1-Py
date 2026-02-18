mnemo = ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан']

colors = ['оранжевый', 'голубой', 'фиолетовый', 'красный', 'желтый', 'синий', 'зеленый']

rainbow_dict = {} # создай словарь rainbow_dict

for i in range(len(mnemo)): # наполни словарь элементами 
    mnemo_str = str(mnemo[i])
    # input()
    # print(mnemo_str)
    for m in range(0, len(colors)):
        colors_str = str(colors[m])
        # input()
        # print(colors_str)
        # print(type(mnemo_str))
        # print(mnemo_str[0])
        if mnemo_str[0] == colors_str[0]:
            rainbow_dict[mnemo[i]] = colors[m]

print(rainbow_dict)