# Делители 1
#
# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.
#
# Примечание. Приведённый ниже код:
#
# print(get_factors(1))
# print(get_factors(5))
# print(get_factors(10))
#
# должен выводить:
#
# [1]
# [1, 5]
# [1, 2, 5, 10]
#
#
# Sample Input 1:
#
# 1
#
# Sample Output 1:
#
# [1]
#
# Sample Input 2:
#
# 5
#
# Sample Output 2:
#
# [1, 5]


# объявление функции
def get_factors(num):
    return [i for i in range(1, num +1) if num % i == 0]

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
