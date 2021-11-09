# Задание a:
list_cub = [i**3 for i in range(1, 1001, 2)]

def sum_cub(number):
    num = 0

    while number != 0:
        num += number % 10
        number //= 10

    return num
result = sum(filter(lambda num: sum_cub(num) % 7 == 0, list_cub))
res2 = sum(filter(lambda num: sum_cub(num + 17) % 7 == 0, list_cub))

print(result)

#Задание b:
list_cub = [i**3 for i in range(1, 1001, 2)]

def sum_cub(number):
    num = 0

    while number != 0:
        num += number % 10
        number //= 10

    return num
result = sum(filter(lambda num: sum_cub(num + 17) % 7 == 0, list_cub))

print(result)
