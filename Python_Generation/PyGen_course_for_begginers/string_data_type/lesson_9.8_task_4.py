# Сортируем слова 📶
#
# На вход программе подаются 33 различных слова. Вам необходимо отсортировать эти слова по возрастанию в лексикографическом порядке и вывести их на одной строке, разделяя символом пробела.
#
# Формат входных данных
# На вход программе подаются 33 слова, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести 33 слова на одной строке, разделяя их символом пробела.
#
#
# Sample Input 1:
#
# python
# java
# kotlin
#
# Sample Output 1:
#
# java kotlin python
#
# Sample Input 2:
#
# первое
# второе
# третье
#
# Sample Output 2:
#
# второе первое третье
#
# Sample Input 3:
#
# июнь
# июль
# август
#
# Sample Output 3:
#
# август июль июнь
#

line1 = input()
line2 = input()
line3 = input()

max_line = max(line1, line2, line3)
min_line = min(line1, line2, line3)
middle_line = ''

for i in [line1, line2, line3]:
    if i != max_line and i != min_line:
        middle_line = i
        break

print(f'{min_line} {middle_line} {max_line}')
