#Задание №2

class DivErr(ZeroDivisionError):
    def __init__(self, txt: str):
        self.txt = txt

dividend = input('Введите делимое: ')
divisor = input('Введите делитель: ')

try:
    dividend = int(dividend)
    divisor = int(divisor)
    if divisor == 0:
        raise DivErr('На ноль делить нельзя')
except ValueError:
    print('То что вы ввели не число')
except DivErr as e:
    print(e)
else:
    print(dividend / divisor)