# Next Prime 🌶️
#
# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число, большее числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
#
# Примечание 2. Приведённый ниже код:
#
# print(get_next_prime(6))
# print(get_next_prime(7))
# print(get_next_prime(14))
#
# должен выводить:
#
# 7
# 11
# 17
#
#
# Sample Input 1:
#
# 6
#
# Sample Output 1:
#
# 7
#
# Sample Input 2:
#
# 7
#
# Sample Output 2:
#
# 11
#

# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# объявление функции
def get_next_prime(num):
    next_prime = 0
    find_next_prime = True
    while find_next_prime:
        for i in range(num + 1, (num + 1) ** 2):
            if is_prime(i):
                next_prime = i
                find_next_prime = False
                break
    return next_prime

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
