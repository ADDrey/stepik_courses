# Вам доступно множество fruits. Напишите программу, которая выводит элементы множества fruits, каждый на отдельной строке, отсортированные по убыванию (в обратном лексикографическом порядке).
#
# Примечание 1. Считайте, что множество fruits уже объявлено в вашей программе, и вы имеете к нему доступ.
#
# Примечание 2. Выводите каждый элемент множества на отдельной строке.
#
#  Sample Input 1:
#
# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
#
# Sample Output 1:
#
# pineapple
# grapefruit
# cherry
# banana
# avocado
# apricot
# apple
#
# Sample Input 2:
#
# fruits = {'orange', 'mango', 'grapes', 'watermelon'}
#
# Sample Output 2:
#
# watermelon
# orange
# mango
# grapes


fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}

print(*sorted(fruits, reverse=True), sep='\n')
