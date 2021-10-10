#Задание №4
prices = [24.3, 53.25, 83.13, 1.32, 15.67, 71.92, 99.9, 67.22, 74.11, 39.28]
result = []
for i in prices:
    for x in str(i).split('.'):
        x = '{:02d}'.format(int(x))
        result.append(x)
for i in range(0, 30, 3):
    result.insert(i+1, 'руб')
for i in range(0, 40, 4):
    result.insert(i+3, 'кп')
print(' '.join(result))
#Как понимаю это было лишним
# rubles = []
# penny = []
# i = 0
# for number in prices:
#     price = '{:02d}'.format(int(number))
#     rubles.append(price)
# for number in prices:
#     price = number % 1
#     new_price = 100 * float('%.2f' % price)
#     penny.append(str(int(new_price)))
# while i != 10:
#     print(f'{rubles[i]} руб {penny[i]} коп')
#     i = i + 1
new_prices = []
for i in sorted(prices):
    for x in str(i).split('.'):
        x = '{:02d}'.format(int(x))
        new_prices.append(x)
for i in range(0, 30, 3):
    new_prices.insert(i+1, 'руб')
for i in range(0, 40, 4):
    new_prices.insert(i+3, 'кп')
print(' '.join(new_prices))
max_prices = sorted(prices, reverse=True)
new_result = []
for i in max_prices:
    for x in str(i).split('.'):
        x = '{:02d}'.format(int(x))
        new_result.append(x)
for i in range(0, 30, 3):
    new_result.insert(i+1, 'руб')
for i in range(0, 40, 4):
    new_result.insert(i+3, 'кп')
print(' '.join(new_result[0:20]))