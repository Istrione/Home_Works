#Задание №3
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

klass_list = {(val for val in tutors) : (key for key in klasses)}
print(dict(klass_list))