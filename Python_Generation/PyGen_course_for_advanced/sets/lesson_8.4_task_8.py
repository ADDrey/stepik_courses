# Одинаковые наборы
#
# На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что для записи этих строк были использованы одинаковые наборы цифр?
#
# Формат входных данных
# На вход подаются две строки, состоящие из цифр.
#
# Формат выходных данных
# Программа должна вывести YES, если для записи этих строк были использованы одинаковые наборы цифр, или NO в противном случае.
#
#  Sample Input 1:
#
# 0943
# 9304
#
# Sample Output 1:
#
# YES
#
# Sample Input 2:
#
# 1
# 2
#
# Sample Output 2:
#
# NO
#
# Sample Input 3:
#
# 327428
# 824723
#
# Sample Output 3:
#
# YES

first_number_digits = set(input())
second_number_digits = set(input())

if first_number_digits == second_number_digits:
    print('YES')
else:
    print('NO')
