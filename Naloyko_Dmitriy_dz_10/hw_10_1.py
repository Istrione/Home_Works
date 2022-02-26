#Задание №1

class Matrix:

    def __init__(self, matr: list):
        self.matr = matr

    def __str__(self):
        matrix = ''
        for i in self.matr:
            matrix += f'{" ".join(map(str, i))}\n'
        return matrix

    def __add__(self, other):
        if len(self.matr) == len(other.matr) and len(self.matr[0]) == len(other.matr[0]) \
                and isinstance(self.matr, list) and isinstance(other.matr, list):
            result = [[self.matr[i][j] + other.matr[i][j]
                       for j in range(len(self.matr[0]))] for i in range(len(self.matr))]
        else:
            msg = f'Размеры матриц не совпадают или это вообще не матрицы'
            raise ValueError(msg)
        return result



a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])


print(a)
print(b)

for _ in (a+b):
    print(*_)