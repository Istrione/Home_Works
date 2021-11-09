#Задание №4

from more import Warehouse, OfficeTech

class Printer(OfficeTech):
    def __init__(self, seal: bool, quantity: int):
        self.seal = seal
        self.quantity = quantity
        OfficeTech.__init__(self, title='Принтер', color='белый')

class Scaner(OfficeTech):
    def __init__(self, scanning: bool, quantity: int):
        self.scanning = scanning
        self.quantity = quantity
        OfficeTech.__init__(self, title='Сканер', color='малиновый')

class Xerox(OfficeTech):
    def __init__(self, whatwecopy: str, quantity: int):
        self.whatwecopy = whatwecopy
        self.quantity = quantity
        OfficeTech.__init__(self, title='Ксерокс', color='желтый')

try:
    a = Xerox('бззз', 1)
    b = Printer(False, 3)
    c = Scaner(True, 2)
    e = Warehouse(10)
    e.additem(a)
    e.additem(b)
    e.additem(c)
    print(e)
    f = Printer(False, 5)
    f.move_to_warehouse(2)
    print(e)
    print(f)
    e.removeitem('Сканер', 1)
    print(e)
except Exception as err:
    print(err)
except ValueError as v:
    print(v)