# Нижний регистр 🔽
#
# На вход программе подаётся строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
#
# Формат входных данных
# На вход программе подаётся строка.
#
# Формат выходных данных
# Программа должна вывести количество буквенных символов в нижнем регистре.
#
#
# Sample Input 1:
#
# abcABCD12345
#
# Sample Output 1:
#
# 3
#
# Sample Input 2:
#
# gggggggg1212321ABDCEFCE
#
# Sample Output 2:
#
# 8
#
# Sample Input 3:
#
# 2376423745dhdhdPPPP
#
# Sample Output 3:
#
# 5

task = input()
lower_case_count = 0
for char in task:
    if char.islower():
        lower_case_count += 1
print(lower_case_count)
