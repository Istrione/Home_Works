#Задание №3 Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

num = int(input('Введите количество чисел в ряде (натуральное число): '))
num_i = 1
summa = 0

for i in range(n):
    summa += num_i
    num_i /= -2

print(f'Сумма чисел последовательности равна: {summa}')