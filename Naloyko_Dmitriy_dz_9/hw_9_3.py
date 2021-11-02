#Задание №3

class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

class Position(Worker):

    def get_full_name(self):
        print(f'Меня зовут {self.surname} {self.name} и я работаю {self.position}ом')

    def get_total_income(self):
        print(f'Я заробатываю {sum(v for v in self._Worker__income.values())} рублей')

worker = Position('Иван', 'Смирнов', 'Грузчик', {'wage': 20000, 'bonus': 5000})
worker.get_full_name()
worker.get_total_income()