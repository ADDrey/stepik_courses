# Строковое представление 💬
#
# Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:
#
#     00 на zero;
#     11 на one;
#     22 на two;
#     33 на three;
#     44 на four;
#     55 на five;
#     66 на six;
#     77 на seven;
#     88 на eight;
#     99 на nine.
#
# Формат входных данных
# На вход программе подается натуральное число.
#
# Формат выходных данных
# Программа должна вывести строковое представление числа.
#
# Примечание. Используйте словарь вместо условного оператора.
#
#  Sample Input 1:
#
# 230
#
# Sample Output 1:
#
# two three zero
#
# Sample Input 2:
#
# 7
#
# Sample Output 2:
#
# seven
#
# Sample Input 3:
#
# 11111111
#
# Sample Output 3:
#
# one one one one one one one one
#
# Sample Input 4:
#
# 83
#
# Sample Output 4:
#
# eight three


dig2_string = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

dig = input()

result = [dig2_string[i] for i in dig if i.isdigit()]
print(*result)