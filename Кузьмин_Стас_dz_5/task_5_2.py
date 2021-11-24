# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

MAX_NUM = 10 ** 4

gen = {num for i in range(1, MAX_NUM + 1) for num in range(1, MAX_NUM + 1) if num % 2 != 0}

print(gen)
print(type(gen))
