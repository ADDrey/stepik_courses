# Вам доступен кортеж countries. Напишите программу, которая выводит количество вхождений строки 'Spain' в кортеж countries.
#
# Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.
#
# Sample Input 1:
#
# countries = ('Mexico', 'New Zealand', 'Spain', 'Poland', 'Latvia', 'Spain')
#
# Sample Output 1:
#
# 2
#
# Sample Input 2:
#
# countries = ('China', 'Moldova', 'Cuba', 'Brazil')
#
# Sample Output 2:
#
# 0


countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
number = countries.count('Spain')
print(number)
