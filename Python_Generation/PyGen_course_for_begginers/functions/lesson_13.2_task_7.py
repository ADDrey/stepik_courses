# Посчитай количества 🔢🌶️
#
# Напишите функцию print_symbol_counts(s), которая принимает на вход слово s и выводит для каждой буквы этого слова в лексикографическом порядке в нижнем регистре на отдельной строке количество её вхождений в это слово в следующем формате:
#
# <L>: <N>
#
# где <L> – некоторая буква слова s, <N> – количество вхождений этой буквы в слово s.
#
# Примечание. Обратите внимание: если в слове встречается одна и та же буква в разных регистрах, то мы считаем это одной и той же буквой (см. тест №4).
#
#
#
# Sample Input 1:
#
# pepper
#
# Sample Output 1:
#
# e: 2
# p: 3
# r: 1
#
# Sample Input 2:
#
# поколение
#
# Sample Output 2:
#
# е: 2
# и: 1
# к: 1
# л: 1
# н: 1
# о: 2
# п: 1
#

# объявление функции
def print_symbol_counts(s):
    lower_s = s.lower()
    characters = {}
    for symbol in lower_s:
        if characters.get(symbol, None) is not None:
            characters[symbol] += 1
        else:
            characters[symbol] = 1
    sorted_characters = dict(sorted(characters.items()))
    for symbol, counter in sorted_characters.items():
        print(symbol, counter, sep=': ')

# считываем данные
s = input()

# вызываем функцию
print_symbol_counts(s)
