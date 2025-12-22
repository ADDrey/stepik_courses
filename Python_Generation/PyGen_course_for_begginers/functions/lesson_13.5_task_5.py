# Is the Number Prime? 🌶️
#
# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True, если число является простым, или False в противном случае.
#
# Примечание 1. Приведённый ниже код:
#
# print(is_prime(1))
# print(is_prime(10))
# print(is_prime(17))
#
# должен выводить:
#
# False
# False
# True
#
# Примечание 2. Простое число – это натуральное число, единственными делителями которого являются только оно само и 11.
#
# Примечание 3. Число 11 простым не является.
#
#
# Sample Input 1:
#
# 1
#
# Sample Output 1:
#
# False
#
# Sample Input 2:
#
# 10
#
# Sample Output 2:
#
# False


# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
