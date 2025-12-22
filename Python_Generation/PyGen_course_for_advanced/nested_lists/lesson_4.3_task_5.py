# Упаковка дубликатов 🌶️
# 
# На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.
# 
# Формат входных данных
# На вход программе подается строка текста, содержащая символы, разделенные символом пробела.
# 
# Формат выходных данных
# Программа должна вывести указанный вложенный список.
# 
# 
# Sample Input 1:
# 
# a b c d
# 
# Sample Output 1:
# 
# [['a'], ['b'], ['c'], ['d']]
# 
# Sample Input 2:
# 
# w w w o r l d g g g g r e a t t e c c h e m g g p w w
# 
# Sample Output 2:
# 
# [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]
# 
# Sample Input 3:
# 
# g i v e t h h i i s m a a a n a g u u n
# 
# Sample Output 3:
# 
# [['g'], ['i'], ['v'], ['e'], ['t'], ['h', 'h'], ['i', 'i'], ['s'], ['m'], ['a', 'a', 'a'], ['n'], ['a'], ['g'], ['u', 'u'], ['n']]

in_str = input().split()
symb_list = [[in_str[0]]]
counter = 0
for symb_num in range(1, len(in_str)):
    if in_str[symb_num - 1] == in_str[symb_num]:
        symb_list[counter].extend(in_str[symb_num])
    else:
        symb_list.append([in_str[symb_num]])
        counter += 1
print(symb_list)

