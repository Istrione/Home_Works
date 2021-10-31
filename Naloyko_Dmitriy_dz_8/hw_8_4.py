#Задание №4

def _logger(func):
    # print('start')
    def wrapper(*args):
        # print('start')
        if 0 < args[0]:
            print(func)
        else:
            raise ValueError(f'Число должно быть положительным')
        # print('finish')
        return func
    # print('finish')
    return wrapper

@_logger
def test_function(x) -> int:
    return x ** 3

test_function(3)
# print('end')
