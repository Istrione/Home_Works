#Задание №3

class ValErr(ValueError):

    def __init__(self, txt: str):
        self.txt = txt

d = input('Введите число: ')
a = []

while d != 'stop':
    try:
        if not d.isdigit():
            raise ValErr('Это не число')
        else:
            d = int(d)
            a.append(d)
    except ValErr as e:
        print(e)
    print(a)
    d = input('Введие число: ')