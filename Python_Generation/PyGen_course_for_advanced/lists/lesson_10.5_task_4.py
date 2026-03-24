# Вам доступен словарь favorite_numbers. Используя генератор словарей, напишите программу, которая выводит словарь, состоящий из всех элементов словаря favorite_numbers, значения которых являются двузначными числами.
#
# Примечание 1. Считайте, что словарь favorite_numbers уже объявлен в вашей программе, и вы имеете к нему доступ.
#
# Примечание 2. Порядок элементов в результирующем словаре не учитывается.
#
#  Sample Input 1:
#
# favorite_numbers = {
#     'scarlett': 41, 'den': 22, 'viktor': 321, 'lera': 777, 'mahad': 4,
#     'manny': 4, 'ken': 8423, 'borya': 12
# }
#
# Sample Output 1:
#
# {'scarlett': 41, 'den': 22, 'borya': 12}
#
# Sample Input 2:
#
# favorite_numbers = {
#     'vika': 28, 'nastya': 24, 'ilya': 20, 'angela': 0, 'ben': 1786,
#     'nadya': 12593, 'katya': 10, 'sergey': 9
# }
#
# Sample Output 2:
#
# {'vika': 28, 'nastya': 24, 'ilya': 20, 'katya': 10}


result = {key: value for key, value in favorite_numbers.items() if 10 <= value <= 99}
print(result)
