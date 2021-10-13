#Задание №1
user_answer = input('Введите число для перевода: ')
translate_list = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
def num_translate(word):

    if user_answer == word:
        print(translate_list.get(word))
    else:
        print(None)

num_translate('one')
# num_translate('three')