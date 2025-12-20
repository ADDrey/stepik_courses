# Negatives, Zeros and Positives
#
# На вход программе подаются натуральное число nn, а затем nn целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
#
# Sample Input 1:
#
# 7
# 3
# -4
# 1
# 0
# -1
# 0
# -2
#
# Sample Output 1:
#
# -4
# -1
# -2
# 0
# 0
# 3
# 1
#
# Sample Input 2:
#
# 5
# 4
# 3
# -2
# -10
# 0
#
# Sample Output 2:
#
# -2
# -10
# 0
# 4
# 3

n = int(input())
numbers = list()
negatives = list()
zeros = list()
positives = list()

for _ in range(n):
    numbers.append(int(input()))

for value in numbers:
    if value < 0:
        negatives.append(value)
    elif value > 0:
        positives.append(value)
    else:
        zeros.append(value)

print(*negatives, *zeros, *positives, sep="\n")
