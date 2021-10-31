#Задание №1
import re

RE_USERNAME = re.compile(r'^\w+[\._-]*\w*@')
RE_DOMAIN = re.compile(r'@\w+\.\w+')

def email_parse(email):
    mail_dict = {}
    try:
        mail_info = RE_USERNAME.findall(email)
        username = re.split(r'@', mail_info[0])
        mail_dict['username'] = username[0]
        mail_info = RE_DOMAIN.findall(email)
        domain = re.split(r'@', mail_info[0])
        mail_dict['domain'] = domain[1]
    except IndexError as e:
        print(f'Произошла ошибка {e}')
        raise ValueError ('Email введен не верно')
    else:
        return mail_dict


#Проверка
# email_parse('someone@yandex.ru')
# email_parse('12someone@mail.ru')
# email_parse('some12one@gmail.com')
# email_parse('some.1ne@yahoo.com')
# email_parse('someone_21@yandex.ru')
