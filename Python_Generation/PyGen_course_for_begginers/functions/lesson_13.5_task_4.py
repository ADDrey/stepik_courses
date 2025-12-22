# Змеиный регистр 🐍
#
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
#
# Примечание 1. Почитать подробнее о стилях именования можно по ссылке.
#
# Примечание 2. Приведённый ниже код:
#
# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))
#
# должен выводить:
#
# this_is_camel_cased
# is_prime_number
#
#
# Sample Input 1:
#
# ThisIsCamelCased
#
# Sample Output 1:
#
# this_is_camel_cased
#
# Sample Input 2:
#
# IsPrimeNumber
#
# Sample Output 2:
#
# is_prime_number
#

# объявление функции
def convert_to_python_case(text):
    new_text = ""
    for i in range(len(text)):
        if text[i].islower():
            new_text += text[i]
        elif text[i].isupper() and i != 0 :
            new_text += "_" + text[i].lower()
        elif i == 0:
            new_text += text[i].lower()
        elif text[i].isdigit():
            new_text += text[i]
    return new_text

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
