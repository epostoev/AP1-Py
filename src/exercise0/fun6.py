# Подключи библиотеку random и дай ей краткое имя
import random as rnd

country_code = '+7'  # код страны пусть будет всегда +7

# используй randint, чтобы сгенерировать трехзначный код оператора
operator_code = rnd.randint(100, 999)

# используй randint, чтобы сгенерировать оставшиеся 7 цифр (без дефисов)
last_digits = rnd.randint(1000000, 9999999)

fake_number = country_code + str(operator_code) + str(last_digits)

print(fake_number)