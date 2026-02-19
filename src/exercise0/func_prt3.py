mail_box = {}   # тут хранятся проверенные письма
spam = []   # сюда складываем спам

# проверка строки на наличие стоп-слов, используется внутри is_spam()
def str_contains_stop_words(string):
    stop_words = ['Без вложений', 'Скидки', 'Распродажа', 'Выгода', 'Гарантия']
    for w in stop_words:
        if w in string:
            return True
    return False

# проверка текста письма на спам, используется внутри mail_checker
def is_spam(mail_text):
    ...


# функция для проверки письма
def mail_checker(mail_to = "None", mail_from = "None", mail_text = "None"):
    mail = {mail_from : mail_text}
    input()
    print(type(mail))
    print(mail))
    if mail_box.get(mail_to):
         mail_box[mail_to].append(mail)
    else:
        mail_box[mail_to] = [mail]

# полученные письма
mail_checker(mail_to='yoda_master@yandex.ru', mail_from='luke_skywalker@yandex.ru', mail_text='Магистр Йода, а в чём сила?')

mail_checker(mail_to='ilon_mask@yandex.ru', mail_from='trusted_mail@yandex.ru', mail_text='Скидки на акции Tesla, только у нас!')

mail_checker(mail_to='chandler_bing@yandex.ru', mail_from='ross_geller@yandex.ru', mail_text='Смотри, я открыл новый вид динозавра https://rossoceraptor.html')

mail_checker(mail_to='piter_parker@yandex.ru', mail_from='j_jonah_jameson@yandex.ru', mail_text='Паркер! Мне срочно нужны фото Паука!')

mail_checker(mail_to='neo@yandex.ru', mail_from='bad_matrix@yandex.ru', mail_text='РАСПРОДАЖА!!! ДВЕ КРАСНЫХ ТАБЛЕТКИ ПО ЦЕНЕ ТРЁХ СИНИХ')

print(mail_box)
# Будет выведено:
# '''
# {
#	'yoda_master@yandex.ru': [
#			{'luke_skywalker@yandex.ru': 'Магистр Йода, а в чем сила?'}
#	], 
#	'piter_parker@yandex.ru': [
#			{'j_jonah_jameson@yandex.ru': 'Паркер! Мне срочно нужны фото Паука!'}
#	]
# }
# '''

print(spam)
# Будет выведено:
# '''
# [
# {'trusted_mail@yandex.ru': 'Скидки на акции Tesla, только у нас!'}, 
# {'ross_geller@yandex.ru': 'Смотри, я открыл новый вид динозавра https://rossoceraptor.html'}, 
# {'bad_matrix@yandex.ru': 'РАСПРОДАЖА!!! ДВЕ КРАСНЫХ ТАБЛЕТКИ ПО ЦЕНЕ ТРЕХ СИНИХ'}]
# '''