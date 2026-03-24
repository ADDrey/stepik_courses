# Вам доступен словарь colors. Используя генератор словарей, напишите программу, которая выводит словарь, состоящий из всех элементов словаря colors, кроме тех, у которых значением является None.
#
# Примечание 1. Считайте, что словарь colors уже объявлен в вашей программе, и вы имеете к нему доступ.
#
# Примечание 2. Порядок элементов в результирующем словаре не учитывается.
#
#  Sample Input 1:
#
# colors = {'a1': 'Blue', 'b2': 'Orange', 'b4': None, 'a6': 'Red', 'c4': None}
#
# Sample Output 1:
#
# {'a1': 'Blue', 'b2': 'Orange', 'a6': 'Red'}
#
# Sample Input 2:
#
# colors = {'b8': 'Grey', 'b9': None, 'a2': 'Green', 'a1': 'Black', 'c10': None, 'a6': 'Pink'}
#
# Sample Output 2:
#
# {'b8': 'Grey', 'a2': 'Green', 'a1': 'Black', 'a6': 'Pink'}


result = {key: value for key, value in colors.items() if value is not None}
print(result)
