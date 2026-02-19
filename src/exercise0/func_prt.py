# создай здесь функцию mail_checker
def mail_checker(mail_to, mail_from, mail_text):
    print(f"Получатель: {mail_to}")
    print(f"Отправитель: {mail_from}")
    print(f"Текст письма: {mail_text}")
	

# mail_checker(mail_to='john_connor@yandex.ru', mail_from='terminator@yandex.ru', mail_text='Привет, я вернулся!')

# должно получиться:
# Получатель: john_connor@yandex.ru
# Отправитель: terminator@yandex.ru
# Текст письма: Привет, я вернулся!


if __name__ == '__main__':
    mail_checker(mail_to='john_connor@yandex.ru', mail_from='terminator@yandex.ru', mail_text='Привет, я вернулся!')