# Переставить min и max 🌶️
#
# На вход программе подаётся строка текста, содержащая различные натуральные числа. Вам необходимо переставить максимальный и минимальный элементы местами и вывести изменённую строку.
#
# Формат входных данных
# На вход программе подаётся строка текста, содержащая различные натуральные числа, разделённые символом пробела.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Используйте подходящие встроенные функции и списочные методы.
#
#
# Sample Input 1:
#
# 3 4 5 2 1
#
# Sample Output 1:
#
# 3 4 1 2 5
#
# Sample Input 2:
#
# 10 9 8 7 6 5 4 3 2 1
#
# Sample Output 2:
#
# 1 9 8 7 6 5 4 3 2 10
#
# Sample Input 3:
#
# 1 2
#
# Sample Output 3:
#
# 2 1
#
# Sample Input 4:
#
# 1
#
# Sample Output 4:
#
# 1

raw_numbers = input().split(' ')
numbers = []
for val in raw_numbers:
    numbers.append(int(val))
minim = min(numbers)
maxim = max(numbers)
min_index = numbers.index(minim)
max_index = numbers.index(maxim)
numbers[min_index] = maxim
numbers[max_index] = minim
print(*numbers)
