#Задание №3
users_hobby = {}
user_list = []
hobby_list = []

with open('More/users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        user = line.split(',')
        user_1 = ' '.join(user).split('\n')
        user_key = ''.join(user_1)
        user_list.append(user_key)

with open('More/hobby.csv', 'r', encoding='utf-8') as h:
    for line in h:
        hobby = line.split(',')
        hobby_1 = ', '.join(hobby).split('\n')
        hobby_value = ''.join(hobby_1)
        hobby_list.append(hobby_value)

for key, value in zip(user_list, hobby_list):
        users_hobby[key] = value

# print(users_hobby)