#Задание №1
users = []

with open('More/nginx_logs.txt', 'r', encoding='utf-8') as f:
    for row in f:
        stroke = row.split('- -')
        stroke_1 = ''.join(stroke).split('"')
        stroke_2 = ''.join(stroke_1).split(' ')
        user = stroke_2[0], stroke_2[4], stroke_2[5]
        users.append(user)

# print(users) #Проверочка