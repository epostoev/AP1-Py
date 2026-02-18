def is_palindrome(string):
    # убираем пробелы
    string_no_space = string.replace(' ', '')
    # получаем строку в обратном порядке
    reversed_string = string_no_space[::-1]
    # допиши код, возвращающий True или False
    if string_no_space == reversed_string:
        is_same = True
    else:
        is_same = False
    return is_same

print(is_palindrome('молебен о коне белом'))  # True

print(is_palindrome('колобок'))  # False

print(is_palindrome('121'))  # True