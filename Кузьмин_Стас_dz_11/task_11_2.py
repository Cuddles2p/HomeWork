# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обра
class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        user_num_1 = int(input('Введите делимое '))
        user_num_2 = int(input('Введите делитель '))
        if user_num_2 == 0:
            raise Error(' Делить на ноль нельзя!')
        else:
            res = user_num_1 / user_num_2
            return res
    except ValueError:
        return 'Неверное число'
    except Error as err:
        return err


print(div())
