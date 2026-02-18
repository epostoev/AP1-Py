
# функция определяет, админ ли текущий пользователь
def is_admin(user):
	if user == "admin":
		is_admin = True
	else:
		is_admin = False
	return is_admin
		

# функция определяет, есть ли доступ у текущего пользователя на страницу
def has_permission(page, user):
	if page == "Управление":
		if is_admin(user) == True:
				is_permission = True 
		else:
				is_permission = False
	elif page != "Управление":
			is_permission = True
	return is_permission

print(has_permission('Рестораны', 'user_a'))

print(has_permission('Избранное', 'admin'))

print(has_permission('Управление', 'admin'))

print(has_permission('Управление', 'user_b'))