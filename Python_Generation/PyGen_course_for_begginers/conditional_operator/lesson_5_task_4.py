# Римские цифры
# 
# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне диапазона [1; 10][1;10], то программа должна вывести текст «ошибка» (без кавычек).
# 
# В таблице приведены римские цифры для чисел от 11 до 1010:
# Число 	Римская цифра
# 11 	I
# 22 	II
# 33 	III
# 44 	IV
# 55 	V
# 66 	VI
# 77 	VII
# 88 	VIII
# 99 	IX
# 1010 	X
# 
# Формат входных данных
# На вход программе подаётся целое число.
# 
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
# 
# 
# Sample Input 1:
# 
# 7
# 
# Sample Output 1:
# 
# VII
# 
# Sample Input 2:
# 
# 12
# 
# Sample Output 2:
# 
# ошибка

value = int(input())
if 0 < value < 11:
    if value == 1:
        print('I')
    elif value == 2:
        print('II')
    elif value == 3:
        print('III')
    elif value == 4:
        print('IV')
    elif value == 5:
        print('V')
    elif value == 6:
        print('VI')
    elif value == 7:
        print('VII')
    elif value == 8:
        print('VIII')
    elif value == 9:
        print('IX')
    else:
        print('X')
else:
    print('ошибка')

