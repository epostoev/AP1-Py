import random as rnd

def get_random_name(name, org=True):
		# сгенерируй Название в зависимости от параметра org
		if org:
			company_name = f"ОАО {name}"
		else:
			company_name = f"ИП {name}"
		return company_name

def get_random_inn(org=True):
		# сгенерируй ИНН в зависимости от параметра org
		if org:
			company_inn = rnd.randint(100000000, 999999999)
		else:
			company_inn = rnd.randint(100000000000, 999999999999)
		return company_inn

def get_random_phone():
    	# сгенерируй телефон
		company_phone = "+7" + str(rnd.randint(1000000000, 9999999999))
		return company_phone

def fake_builder(name, org=True):
		return {
			'Название': get_random_name(name = name, org = org),# используй функцию для генерации имени
			'ИНН': get_random_inn(org = org),# используй функцию для генерации ИНН,
			'Телефон': get_random_phone() # используй функцию для генерации телефона
		}

print(fake_builder(name = 'Дом у дороги'))
print(fake_builder(name = 'Шрут Дуайт Курт', org=False))