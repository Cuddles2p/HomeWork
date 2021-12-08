# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?

import re

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+"

path_log = r'main2.py'


def parse_email(path, pattern):
    with open(f'{path}', 'r', encoding='utf-8') as f_mail:
        for el in f_mail.readlines():
            if re.findall(pattern, el.strip()):
                print({'username': el.split('@')[0], 'domain': el.split('@')[1].strip()})
            else:
                raise ValueError(f'ValueError: wrong email: {el}')


parse_email(path_log, pattern)
