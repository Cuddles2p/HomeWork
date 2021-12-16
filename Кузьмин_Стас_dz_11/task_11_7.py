# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class ComplexNums:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    def __add__(self, other):
        return f'Сумма равна: {self.nums1 + other.nums1} + {self.nums2 + other.nums2} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.nums1 * other.nums1 - (self.nums2 * other.nums2)} + {self.nums2 * other.nums1} * i'


c_1 = ComplexNums(10, -8)
c_2 = ComplexNums(5, 2)
print(c_1 + c_2)
print(c_1 * c_2)
