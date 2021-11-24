# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
#
# Подсказка: использовать возможности python, изученные на уроке. Подумайте,
# как можно сделать оптимизацию кода по памяти, по скорости.
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def more(input_list: list):
    result = []
    for key, value in enumerate(input_list):
        if key + 1 < len(input_list) and value < input_list[key + 1]:
            result.append(input_list[key + 1])
    return result


print(more(src))
#  Вариант решение в одну строку
result1 = []

gen = {result1 for key, value in enumerate(src) if
       key + 1 < len(src) and value < src[key + 1] and result1.append(src[key + 1])}
print(result1)
