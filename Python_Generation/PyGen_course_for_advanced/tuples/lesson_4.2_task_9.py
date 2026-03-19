# Вам доступен кортеж countries. Напишите программу, которая выводит индекс строки 'Slovenia' в кортеже countries.
#
# Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.
#
# Sample Input 1:
#
# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
#
# Sample Output 1:
#
# 5
#
# Sample Input 2:
#
# countries = ('China', 'Slovenia', 'Cuba', 'Brazil')
#
# Sample Output 2:
#
# 1

countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
index = countries.index('Slovenia')
print(index)
