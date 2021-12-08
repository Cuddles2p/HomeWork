# Написать декоратор для логирования типов позиционных аргументов функции, например:
#
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__}(', end='')

        res_args = []
        for arg in args:
            res_args.append(f'{str(arg)}: {type(arg)}')
            if kwargs:
                print(','.join(res_args), end=',')
            else:
                print(','.join(res_args), end=')')

            res_kwargs = []
            for key, value in kwargs.items():
                res_kwargs.append(f'{str(key)}: {type(key)}, {str(value)} : {type(value)}')
            print(','.join(res_kwargs), end=')\n')

            return func(*args, **kwargs)

    return wrapper


@type_logger
def calc_cube(x, **kwargs):
    return x ** 3


a = calc_cube(10, h=13)
