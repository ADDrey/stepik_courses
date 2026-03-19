# Вам доступен кортеж numbers. Напишите программу, которая выводит произведение элементов кортежа numbers.
#
# Примечание. Считайте, что кортеж numbers уже объявлен в вашей программе, и вы имеете к нему доступ.
#
# Sample Input 1:
#
# numbers = (1, -4, 3, 2, 5, 7)
#
# Sample Output 1:
#
# -840
#
# Sample Input 2:
#
# numbers = (3, 85, 0, -4, 3, 4, 14, 2, -1)
#
# Sample Output 2:
#
# 0

numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
result = 1

for number in numbers:
    result *= number
print(result)
