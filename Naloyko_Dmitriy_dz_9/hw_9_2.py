#Задание №2

class Road:

    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width

    def asphalt_mass(self, mass: int, depth: int):
        self.mass = mass
        self.depth = depth
        print(f'{self.__length} м*{self.__width} м*{self.mass} кг*{self.depth} см = '
              f'{self.__length * self.__width * self.mass * self.depth // 1000}т')

trasse = Road(1000, 200)
trasse.asphalt_mass(25, 5)