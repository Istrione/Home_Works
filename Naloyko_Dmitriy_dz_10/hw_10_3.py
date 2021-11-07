#Задание №3

class Cage:

    def __init__(self, cell: int):
        self.cell = cell

    def __add__(self, other):
        if isinstance(self.cell, int) and isinstance(other.cell, int):
            cells = self.cell + other.cell
        else:
            cells = f'Нельзя выполнить сложение'
        return cells

    def __sub__(self, other):
        if isinstance(self.cell, int) and isinstance(other.cell, int) and self.cell > other.cell:
            cells = self.cell - other.cell
        else:
            cells = f'Нельзя выполнить вычитание'
        return cells

    def __mul__(self, other):
        if isinstance(self.cell, int) and isinstance(other.cell, int):
            cells = self.cell * other.cell
        else:
            cells = f'Нельзя выполнить умножение'
        return cells

    def __floordiv__(self, other):
        if isinstance(self.cell, int) and isinstance(other.cell, int) and other.cell > 0:
            cells = self.cell // other.cell
        else:
            cells = f'Нельзя выполнить деление'
        return cells

    def __truediv__(self, other):
        if isinstance(self.cell, int) and isinstance(other.cell, int) and other.cell > 0:
            cells = self.cell / other.cell
        else:
            cells = f'Нельзя выполнить деление'
        return cells

    def make_order(self, cell_size: int):
        if self.cell <= cell_size:
            result = f"{'*' * self.cell}"
        else:
            full_cells = self.cell // cell_size
            other_cells = self.cell % cell_size
            result = (f'{"*" * cell_size}\n' * full_cells) + ("*" * other_cells)
        return result

a = Cage(13)
b = Cage(6)
c = Cage(a + b)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a / b)
print(c.make_order(5))