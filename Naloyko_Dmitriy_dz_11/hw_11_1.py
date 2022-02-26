#Задание №1

import re

class Date:

    def __init__(self, date: str):
        self.date = date

    @staticmethod
    def validator(date):
        re_date = re.split(r'[^0-9]+', date)
        if len(re_date) == 3 and 1 <= int(re_date[0]) <= 31 and 1 <= int(re_date[1]) <= 12 \
                and 1 <= int(re_date[2]) <= 2021:
            return re_date
        else:
            msg = 'Вы ввели дату не в том формате'
            raise ValueError(msg)

    @classmethod
    def int_giver(cls, param):
        answer = Date.validator(param)
        return answer

#Проверка
try:
    print(*Date.int_giver('26-03-1986'))
except ValueError as val:
    print(f'{val}')