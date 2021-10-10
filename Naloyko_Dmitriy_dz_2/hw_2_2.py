#Задание №2
text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for value in text:
    if ord(value[0]) in range(48, 58):
            new_value = '{:02d}'.format(int(value))
            text[text.index(value)] = new_value
    if ord(value[0]) == 43 or ord(value[0]) == 45:
            new_value = '{:02d}'.format(int(value[1:]))
            text[text.index(value)] = value[:1] + new_value
print(' '.join(text))