def is_authorized_user(user):
	# твой код 
    if user[0] and user[1] or user[2]:
        print("OK")


user_1 = ['login', 'password', '']

is_authorized_user(user_1)

user_2 = ['', '', 'token']

is_authorized_user(user_2)

user_3 = ['login', '', '']

is_authorized_user(user_3)

user_4 = ['', '', '']

is_authorized_user(user_4)