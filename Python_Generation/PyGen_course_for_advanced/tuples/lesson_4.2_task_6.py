# Вам доступен кортеж countries. Напишите программу, которая выводит все элементы кортежа countries, кроме двух последних и трех первых.
#
# Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.
#
# Sample Input 1:
#
# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
#
# Sample Output 1:
#
# ('Bulgaria', 'Slovakia')
#
# Sample Input 2:
#
# countries = ('Australia', 'Russia', 'Nigeria', 'Chad', 'Canada', 'USA', 'Germany', 'Netherlands')
#
# Sample Output 2:
#
# ('Chad', 'Canada', 'USA')


countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:-2])
