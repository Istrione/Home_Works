#Задание №7

import re

class ComNum:

    def __init__(self, number: str):
        self.number = number

    def validator(self, num: str):
        re_date = re.split(r"\' '+|[^0-9-]+", num)
        if re.match(r'^\-([0-9])+|^([0-9])+', re_date[0]) is not None \
                and re.match(r'^\-([0-9])+|^([0-9])+', re_date[1]) is not None:
            return re_date[:2]
        else:
            msg = f'{num} не комплексное число'
            raise ValueError(msg)

    def __add__(self, other):
        date_1 = self.validator(self.number)
        date_2 = self.validator(other.number)
        return ComNum(f'{int(date_1[0]) + int(date_2[0])} + {int(date_1[1]) + int(date_2[1])}i')

    def __mul__(self, other):
        date_1 = self.validator(self.number)
        date_2 = self.validator(other.number)
        result_1 = int(date_1[0]) * int(date_2[0]) - int(date_1[1]) * int(date_2[1])
        result_2 = int(date_1[0]) * int(date_2[1]) + int(date_1[1]) * int(date_2[0])
        return ComNum(f'{result_1} + {result_2}i')

    def __str__(self):
        return f'{self.number}'

a = ComNum('5+5i')
b = ComNum('3 + -3i')

try:
    c = a + b
    print(c)
    d = a * b
    print(d)
except ValueError as e:
    print(e)