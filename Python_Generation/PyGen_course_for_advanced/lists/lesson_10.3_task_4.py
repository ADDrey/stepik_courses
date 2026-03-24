# Вам доступна строка text, содержащая слова в нижнем регистре, разделенные символом пробела. Напишите программу, которая выводит наиболее часто встречающееся слово строки text. Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.
#
# Примечание. Считайте, что строка text уже объявлена в вашей программе, и вы имеете к ней доступ.
#
#  Sample Input 1:
#
# text = 'bridge snake island game glory eye arrogant car nature game glory game'
#
# Sample Output 1:
#
# game
#
# Sample Input 2:
#
# text = 'coat pencil guy tree tree pause power sand apple song taxi tree coat coat pause pause'
#
# Sample Output 2:
#
# coat

words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Ищем слово с максимальной частотой, но при равенстве — минимальное лексикографически
result = min(freq, key=lambda word: (-freq[word], word))
print(result)