# Секретное слово
#
# Напишите программу для расшифровки секретного слова методом частотного анализа.
#
# Формат входных данных
# В первой строке задано зашифрованное слово. Во второй строке задано одно целое число nn – количество букв в словаре. В следующих nn строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.
#
# Формат выходных данных
# Программа должна вывести дешифрованное слово.
#
# Примечание. Гарантируется, что частоты букв не повторяются.
#
#  Sample Input 1:
#
# *!*!*?
# 3
# а: 3
# н: 2
# с: 1
#
# Sample Output 1:
#
# ананас
#
# Sample Input 2:
#
# pop
# 2
# д: 2
# е: 1
#
# Sample Output 2:
#
# дед


encrypted = input().strip()
n = int(input())
freq_to_letter = {}

for _ in range(n):
    line = input().strip()
    # Разделяем по ": "
    letter, freq_str = line.split(': ')
    freq = int(freq_str)
    freq_to_letter[freq] = letter

# Считаем частоту каждого символа в зашифрованном слове
from collections import Counter
char_freq = Counter(encrypted)

# Расшифровываем
decrypted = []
for char in encrypted:
    freq = char_freq[char]
    decrypted.append(freq_to_letter[freq])

print(''.join(decrypted))