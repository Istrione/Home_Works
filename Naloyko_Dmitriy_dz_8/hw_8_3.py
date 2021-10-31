#Задание №3

def type_logger(func):
    # print('Я-Декоратор')
    def wrapper(*args, **kwargs):
        # print('Я-Обертка')
        result = print(f'{func.__name__}{args[0], type(*args)}')
        # print('Я закончил')
        return result
    # print('Я тоже')
    return wrapper

@type_logger
def test_function(x):
    return x ** 3
#Проверка
# test_function(3)