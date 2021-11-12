# Вариант заданиа а
list_cub = []

for i in range (1,1001):
    if (i % 2!=0):
        i=i**3
        list_cub.append(i)

numbers_sum = 0
numbers_list =[]
for i in range(len(list_cub)):
    my_str = str(list_cub[i])
    my_list = list (my_str)

    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    for i in range(len(my_list)):
        numbers_sum = numbers_sum + my_list[i]
    if numbers_sum % 7 == 0:

        numbers_list.append(numbers_sum)
print(numbers_list)

# Вариант заданиа b
list_cub = []

for i in range (1,1001):
    if (i % 2!=0):
        i=i**3+17
        list_cub.append(i)

numbers_sum = 0
numbers_list =[]
for i in range(len(list_cub)):
    my_str = str(list_cub[i])
    my_list = list (my_str)

    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    for i in range(len(my_list)):
        numbers_sum = numbers_sum + my_list[i]
    if numbers_sum % 7 == 0:
        numbers_list.append(numbers_sum)
print(numbers_list)

# Вариант заданиа c
list_cub = []

for i in range (1,1001):
    if (i % 2!=0):
        i=i**3+17
        list_cub.append(i)

numbers_sum = 0

for i in range(len(list_cub)):
    my_str = str(list_cub[i])
    list_cub.clear
    my_list = list (my_str)

    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    for i in range(len(my_list)):
        numbers_sum = numbers_sum + my_list[i]
    if numbers_sum % 7 == 0:
        numbers_list.append(numbers_sum)
print(numbers_list)