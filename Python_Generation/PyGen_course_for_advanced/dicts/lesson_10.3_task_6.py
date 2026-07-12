# Самое редкое слово 🌶️
#
# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.
#
# Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.
#
# Примечание 2. Слово – последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.
#
#
#  Sample Input 1:
#
# home sweet home
#
# Sample Output 1:
#
# sweet
#
# Sample Input 2:
#
# home sweet home sweet.
#
# Sample Output 2:
#
# home

text = input()

words = []
for word in text.split():
    clean_word = ''.join(char for char in word if char.isalpha())
    if clean_word:
        words.append(clean_word.lower())

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

min_freq = min(freq.values())

rarest = min(word for word, count in freq.items() if count == min_freq)

print(rarest)