def is_authorized_user(login='', password='', token=''):
	# тело функции менять не нужно
	if login and password or token:
			print('OK')

user_1 = ['', '', '']

# тут просто 3 параметра - 3 значения в списке
is_authorized_user(user_1[0], user_1[1], user_1[2])

user_2 = ['login', 'password']

# у user_2 теперь всего 2 параметра
is_authorized_user(user_2[0], user_2[1])

user_3 = ['token']

# у user_3 только токен
is_authorized_user(token = user_3[0])

user_4 = ['login', '']

# у user_4 токена нет, но и пароль отсутсвует
is_authorized_user(login = user_4[0])