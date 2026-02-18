def condition_check(condition_a, condition_b):
    if condition_a != condition_b:
        is_check = False
    else:
        is_check = True
    return is_check


# вызовы функций не меняй
print(condition_check('a', 'b'))   # False

print(condition_check(1, '1'))     # False

print(condition_check(['Кнопка 1', 'Поле 2'], ['Кнопка 1', 'Поле 1'])) # False

print(condition_check(['Кнопка 1', 'Поле 1'], ['Кнопка 1', 'Поле 1'])) # True