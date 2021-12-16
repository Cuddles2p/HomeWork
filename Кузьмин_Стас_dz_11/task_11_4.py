# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
class Warehouse:

    def __init__(self, name, price, quatity):
        self.name = name
        self.price = price
        self.quatity = quatity
        self.items = {'Модель устройства': self.name, 'Цена за единицу': self.price, 'Количество': self.quatity}

    def income(self):
        try:
            name = input(f'Введите наименования')
            price = int(input(f'Введите цену за единицу'))
            quatity = int(input(f'Введите количество'))
            item = {'Модель устройства': name, 'Цена за единицу': price, 'Количество': quatity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            price('Недопустимое значение!')


class Printer(Warehouse):
    pass


class Scanner(Warehouse):
    pass


class Xerox(Warehouse):
    pass


p = Printer('PANTUM', 3, 3750)
s = Scanner('Canon', 1, 3000)
x = Xerox('Xerox', 2, 3250)

p.income()
s.income()
x.income()
