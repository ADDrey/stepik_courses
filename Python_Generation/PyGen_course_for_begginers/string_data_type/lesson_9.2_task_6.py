# Делаем срезы 1
#
# На вход программе подаётся одна строка. Напишите программу, которая выводит:
#
#     общее количество символов в строке;
#     исходную строку, повторённую 33 раза;
#     первый символ строки;
#     первые три символа строки;
#     последние три символа строки;
#     строку в обратном порядке;
#     строку с удалённым первым и последним символами.
#
# Формат входных данных
# На вход программе подаётся одна строка, длина которой больше 33 символов.
#
# Формат выходных данных
# Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной строке.
#
#
# Sample Input 1:
#
# abcdefghijklmnopqrstuvwxyz
#
# Sample Output 1:
#
# 26
# abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
# a
# abc
# xyz
# zyxwvutsrqponmlkjihgfedcba
# bcdefghijklmnopqrstuvwxy
#
# Sample Input 2:
#
# Success is the ability to go from failure to failure without losing your enthusiasm
#
# Sample Output 2:
#
# 83
# Success is the ability to go from failure to failure without losing your enthusiasmSuccess is the ability to go from failure to failure without losing your enthusiasmSuccess is the ability to go from failure to failure without losing your enthusiasm
# S
# Suc
# asm
# msaisuhtne ruoy gnisol tuohtiw eruliaf ot eruliaf morf og ot ytiliba eht si sseccuS
# uccess is the ability to go from failure to failure without losing your enthusias

s = input()

## общее количество символов в строке
print(len(s))

## исходную строку повторенную 3 раза
print(s, s, s, sep='')

## первый символ строки
print(s[0])

## первые три символа строки
print(s[:3])

## последние три символа строки
print(s[-3:])

## строку в обратном порядке
print(s[::-1])

## строку с удаленным первым и последним символом
print(s[1:len(s)-1])
