#Задание №1

import time as tm

class Trafficlight:
    color = ['Красный', 'Жёлтый', 'Зелёный']
    time = [7, 2, 8]

    def running(self):
        i = 0
        while i != 3:
            while self.time[i]:
                print(f'{self.color[i]} будет гореть еще {self.time[i]} секунд')
                tm.sleep(1)
                self.time[i] -= 1
            i += 1

flashlight = Trafficlight()
flashlight.running()