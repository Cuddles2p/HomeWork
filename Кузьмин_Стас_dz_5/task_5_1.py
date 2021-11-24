# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
#

MAX_NUMS = 15


def nums_gen():
    for num in range(1, MAX_NUMS + 1, 2):
        if num % 1 == 0:
            yield num


nums = nums_gen()

print(type(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
