# Волшебное число ✨
#
# В некотором наборе слов Сэм находит "волшебное" число по следующему алгоритму: берет самую "маленькую" и самую "большую" строки, перемножает Unicode-коды последних символов этих строк и возводит полученное число в квадрат. Результатом и является "волшебное" число.
#
# На вход программе подаются 44 слова. Найдите "волшебное" число в этом наборе слов.
#
# Формат входных данных
# На вход программе подаются 44 слова, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести "волшебное" число в наборе слов.
#
#
# Sample Input 1:
#
# I
# will
# be
# back
#
# Sample Output 1:
#
# 62157456
#
# Sample Input 2:
#
# all
# dreams
# come
# true
#
# Sample Output 2:
#
# 118984464

line = input()
biggest_line = line
smallest_line = line
lines_count = 4

for _ in range(lines_count - 1):
    line = input()
    biggest_line = max(line, biggest_line)
    smallest_line = min(line,smallest_line)

magic_number = (ord(biggest_line[-1]) * ord(smallest_line[-1])) ** 2
print(magic_number)
