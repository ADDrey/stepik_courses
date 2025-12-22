# BEEGEEK 🐝🌶️
#
# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#
#     число a – должно быть палиндромом;
#     число b – должно быть простым;
#     число c – должно быть чётным.
#
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка, или False в противном случае.
#
# Примечание. Приведённый ниже код:
#
# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))
#
# должен выводить:
#
# True
# False
# False
# False
#
#
# Sample Input 1:
#
# 15551:7:290
#
# Sample Output 1:
#
# True
#
# Sample Input 2:
#
# 155561:7:290
#
# Sample Output 2:
#
# False
#

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_palindrome(text):
    only_text = text.lower()
    reversed_text = ''.join(reversed(only_text))
    if only_text == reversed_text:
        return True
    return False

def is_valid_password(password):
    password_elements = password.split(':')
    if len(password_elements) > 3:
        return False
    a, b, c = password_elements[0], password_elements[1], password_elements[2]
    if is_even(int(c)) and is_prime(int(b)) and is_palindrome(a):
        return True
    return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
