#Задание №4

class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print(f'{self.__class__.__name__} поехала')

    def car_stop(self):
        print(f'{self.__class__.__name__} остановилась')

    def car_turn(self, direction: str):
        self.direction = direction
        print(f'{self.__class__.__name__} повернула {self.direction}')

    def show_speed(self):
        print(f'{self.__class__.__name__} движется со скоростью {self.speed} км/ч')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.__class__.__name__} превышает положеную скорость движения на '
                  f'{self.speed - 60} км/ч')
        else:
            print(f'{self.__class__.__name__} движется со скоростью {self.speed} км/ч')

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.__class__.__name__} превышает положеную скорость движения на '
                  f'{self.speed - 40} км/ч')
        else:
            print(f'{self.__class__.__name__} движется со скоростью {self.speed} км/ч')

class SportCar(Car):

    def noise(self):
        print('Бу-бу-бу-бу')

class PoliceCar(Car):

    def persecution(self):
        if self.is_police == True:
            print(f'{self.__class__.__name__} введет приследование')
        else:
            print(f'{self.__class__.__name__} патрулирует город')

car = Car(60, 'Черная', 'Mazda')
print(car.name, car.color, car.speed)
car.car_go()
car.car_stop()
car.car_turn('налево')
car.show_speed()

town_car = TownCar(65, 'белый', 'Gazell')
town_car.car_go()
town_car.car_stop()
town_car.car_turn('направо')
town_car.show_speed()

work_car = WorkCar(40, 'жёлтый', 'Kamaz')
work_car.car_go()
work_car.car_stop()
work_car.car_turn('направо')
work_car.show_speed()

sport_car = SportCar(110, 'красный', 'Nissan')
sport_car.car_go()
sport_car.noise()
sport_car.car_stop()
sport_car.car_turn('налево')
sport_car.show_speed()

police_car = PoliceCar(110, 'синий', 'BMW', is_police=True)
police_car.car_go()
police_car.car_stop()
police_car.car_turn('налево')
police_car.show_speed()
police_car.persecution()