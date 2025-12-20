# Без дубликатов
#
# На вход программе подаются натуральное число nn, а затем nn строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Считайте, что все строки состоят из строчных символов.
#
#
# Sample Input:
#
# 5
# first
# second
# first
# third
# second
#
# Sample Output:
#
# first
# second
# third


n = int(input())
strings = list()

for _ in range(n):
    strings.append(input())

unique_stings = list()

for i in strings:
    if i not in unique_stings:
        unique_stings.append(i)

print(*unique_stings, sep='\n')
