mail_box = {}  # изначально наш ящик пустой и в нем нет писем

# напиши здесь функцию, которая добавляет письма в mail_box
def mail_checker(mail_to = "None", mail_from = "None", mail_text = "None"):
    mail = {mail_from : mail_text}
    if mail_box.get(mail_to):
         mail_box[mail_to].append(mail)
    else:
        mail_box[mail_to] = [mail]

if __name__ == '__main__':
# полученные письма

    mail_checker(mail_to='john_connor@yandex.ru', mail_from='terminator@yandex.ru', mail_text='Привет, я вернулся!')

    mail_checker(mail_to='john_connor@yandex.ru', mail_from='sarah_connor@yandex.ru', mail_text='Сынок, надень шапку')

    mail_checker(mail_to='luke_skywalker@yandex.ru', mail_from='darth_vader@yandex.ru', mail_text='Правая рука чешется, не знаю, что и делать')

    mail_checker(mail_to='luke_skywalker@yandex.ru', mail_from='darth_vader@yandex.ru', mail_text='Что бы сказал на это твой отец?')

    print(mail_box)
# Будет выведено:
# {
# 	'john_connor@yandex.ru': [
# 		{'terminator@yandex.ru': 'Привет, я вернулся!'}, 
# 		{'sarah_connor@yandex.ru': 'Сынок, надень шапку'}
# 	], 
# 	'luke_skywalker@yandex.ru': [
# 		{'darth_vader@yandex.ru': 'Правая рука чешется, не знаю, что и делать'},
# 		{'darth_vader@yandex.ru': 'Что бы сказал на это твой отец?'}
# 	]
# }