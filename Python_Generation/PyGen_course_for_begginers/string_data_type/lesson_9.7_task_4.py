# Самое тяжёлое слово 🗿
#
# Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова. Напишите программу, которая принимает 44 слова и находит среди них самое тяжёлое слово. Если самых тяжёлых слов будет несколько, то программа должна вывести первое из них.
#
# Формат входных данных
# На вход программе подаются 44 слова, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести самое тяжёлое слово в строке.
#
#
# Sample Input 1:
#
# строки
# списки
# кортежи
# множества
#
# Sample Output 1:
#
# множества
#
# Sample Input 2:
#
# az
# by
# cx
# 122
#
# Sample Output 2:
#
# az

word_1, word_2, word_3, word_4 = input(), input(), input(), input()
words_list = [word_1, word_2, word_3, word_4]

weightest_word = word_1
max_weight_word = sum([ord(letter) for letter in word_1])

weight_word_2 = sum([ord(letter) for letter in word_2])
if weight_word_2 > max_weight_word:
    weightest_word = word_2
    max_weight_word = weight_word_2

weight_word_3 = sum([ord(letter) for letter in word_3])
if weight_word_3 > max_weight_word:
    weightest_word = word_3
    max_weight_word = weight_word_3

weight_word_4 = sum([ord(letter) for letter in word_4])
if weight_word_4 > max_weight_word:
    weightest_word = word_4
    max_weight_word = weight_word_4

print(weightest_word)
