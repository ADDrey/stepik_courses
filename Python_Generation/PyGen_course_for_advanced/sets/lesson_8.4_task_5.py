# Количество различных символов
#
# На вход программе подается строка текста. Напишите программу, которая определяет количество различных символов в строке.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести количество различных символов в строке.
#
#
#  Sample Input 1:
#
# 12345678910
#
# Sample Output 1:
#
# 10
#
# Sample Input 2:
#
# ab bc
#
# Sample Output 2:
#
# 4


text =input()

unique_text_symbols = set(text)

count_of_unique_text_symbols = len(unique_text_symbols)

print(count_of_unique_text_symbols)
