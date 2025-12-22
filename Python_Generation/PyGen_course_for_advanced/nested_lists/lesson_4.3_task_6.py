# Разбиение на чанки 🌶️
# 
# На вход программе подаются две строки: на одной – символы, на другой – число nn. Из первой строки формируется список.
# 
# Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков (кусков) указанной длины.
# 
# Формат входных данных
# На вход программе подаются строка текста, содержащая символы, разделенные символом пробела, и число nn на отдельной строке.
# 
# Формат выходных данных
# Программа должна вывести указанный вложенный список.
# 
# Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат. 😀
# 
# 
# Sample Input 1:
# 
# a b c d e f
# 2
# 
# Sample Output 1:
# 
# [['a', 'b'], ['c', 'd'], ['e', 'f']]
# 
# Sample Input 2:
# 
# a b c d e f
# 3
# 
# Sample Output 2:
# 
# [['a', 'b', 'c'], ['d', 'e', 'f']]
# 
# Sample Input 3:
# 
# a b c d e f
# 6
# 
# Sample Output 3:
# 
# [['a', 'b', 'c', 'd', 'e', 'f']]
# 
# Sample Input 4:
# 
# a b c d e f r g b
# 2
# 
# Sample Output 4:
# 
# [['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
# 
# Sample Input 5:
# 
# a b
# 3
# 
# Sample Output 5:
# 
# [['a', 'b']]


def chunked(lst, chunk):
    chunked_lst = [[lst[0]]]
    counter = 0
    for i in range(1, len(lst)):
        if i % chunk:
            chunked_lst[counter].append(lst[i])
        else:
            chunked_lst.append([lst[i]])
            counter += 1
    return chunked_lst
            

in_lst = input().split()
in_num = int(input())

print(chunked(in_lst, in_num))
