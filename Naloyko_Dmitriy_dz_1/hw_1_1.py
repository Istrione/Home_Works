# # 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#
# # Задание №1
# duration = 5294861
# day = duration // 86400
# duration = duration - day * 86400
# hour = duration // 3600
# duration = duration - hour * 3600
# minute = duration // 60
# duration = duration - minute * 60
# print(day, ' дн ', hour, ' час ', minute, ' мин ', duration, ' сек')

# Задание №2
# вариант а
old_list = []
for i in range(1, 1000, 2):
    number = i ** 3
    numbers = [int(x) for x in str(number)]
    if sum(numbers) % 7 == 0:
        old_list.append(numbers)
old_list_2 = [int("".join([str(n) for n in y])) for y in old_list]
print(sum(old_list_2))
# вариант b
old_list = []
for i in range(1, 1000, 2):
    number = i ** 3 + 17
    numbers = [int(x) for x in str(number)]
    if sum(numbers) % 7 == 0:
        old_list.append(numbers)
old_list_2 = [int("".join([str(n) for n in y])) for y in old_list]
print(sum(old_list_2))

# Задание №3
for p in range(1, 101):
    if p == 1:
        print(p, ' процент')
    elif p > 1 and p < 5:
        print(p, ' процента')
    else:
        print(p, ' процентов')