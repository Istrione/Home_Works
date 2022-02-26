#Задание №5

class Stationery:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print(f'Написать ручкой письмо')

class Pencil(Stationery):

    def draw(self):
        print(f'Начертить {self.title}ом чертёж')

class Handle(Stationery):

    def draw(self):
        print(f'Нарисовать {self.title}ом')

pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()