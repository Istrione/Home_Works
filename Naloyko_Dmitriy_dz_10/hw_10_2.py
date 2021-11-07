#Задание №2

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, size: int):
        self.size = size

    @abstractmethod
    def quantity_of_fabric(self):
        pass

class Coat(Clothes):

    @property
    def quantity_of_fabric(self):
        fabric = self.size / 6.5 + 0.5
        return fabric



class Dress(Clothes):

    @property
    def quantity_of_fabric(self):
        fabric = self.size * 2 + 0.3
        return fabric



a = Coat(5)
b = Dress(5)

print(float('{:.2f}'.format(a.quantity_of_fabric)))
print(float('{:.2f}'.format(b.quantity_of_fabric)))