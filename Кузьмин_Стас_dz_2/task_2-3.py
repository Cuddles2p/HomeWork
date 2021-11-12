# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

def find_sign(num):
    if num[0] in '+-':
        return num[0]


number_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(number_list):
    sign = find_sign(number_list[i])
    if number_list[i].isdigit() or (sign and number_list[i][1:].isdigit()):
        if sign:
            number_list[i] = sign + number_list[i][1:].zfill(2)
        else:
            number_list[i] = number_list[i].zfill(2)

        number_list.insert(i, '"')
        number_list.insert(i + 2, '"')
        i += 2

    i += 1
str_list = ' '.join(number_list)
print(str_list)
