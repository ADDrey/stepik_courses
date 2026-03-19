# Вам доступен кортеж countries. Напишите программу, которая выводит все элементы кортежа countries, кроме последних трех.
#
# Примечание. Считайте, что кортеж countries уже объявлен в вашей программе, и вы имеете к нему доступ.
#
# Sample Input 1:
#
# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
#
# Sample Output 1:
#
# ('Romania', 'Poland', 'Estonia', 'Bulgaria')
#
# Sample Input 2:
#
# countries = ('Chad', 'Canada', 'USA', 'Germany', 'Netherlands')
#
# Sample Output 2:
#
# ('Chad', 'Canada')


countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[:len(countries)-3])
