#Задание №2 Написать код для задачи: "Обработка сетевых пакетов"
from collections import deque

size, n = map(int, input().split())
queue = deque()

for i in range(n):
    arrival, duraction = map(int, input().split())

    while queue and queue[0] <= arrival:
        queue.popleft()

    if len(queue) < size:
        if queue:
            arrival = max(arrival, queue[-1])
        print(arrival)
        queue.append(arrival + duration)
    else:
        print(-1)