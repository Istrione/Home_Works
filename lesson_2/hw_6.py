#Задание №6 Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр. Дополнительно (рекурсивно)

n = int(input('Введите числа, если хотите закончить ввод. Введите 0: '))
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m
    n = int(input())

print(f"Число {max_m}, имеет максимальную сумму цифр: {max_s}")