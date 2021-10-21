#Задание №1
def gen_number(number):

    for num in range(1, number + 1, 2):
        yield num #как я понял из методички можно было бы использовать и return, только он бы обнулялся каждый раз

# test = gen_number(15)
# print(next(test), next(test))