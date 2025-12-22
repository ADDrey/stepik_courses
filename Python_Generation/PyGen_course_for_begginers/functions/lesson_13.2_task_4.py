# Отсортируй и выведи 📶
#
# Напишите функцию print_sorted_hyphen(s), которая принимает строку s, состоящую из слов, разделённых дефисами, и выводит эти слова на одной строке в лексикографическом порядке, разделённые дефисами.
#
# Примечание. Гарантируется, что в последовательности будет более одного слова.
#
#
# Sample Input 1:
#
# orange-apple-avocado-plum-cherry
#
# Sample Output 1:
#
# apple-avocado-cherry-orange-plum
#
# Sample Input 2:
#
# Сослан-Света-Валера-Артур-Антон
#
# Sample Output 2:
#
# Антон-Артур-Валера-Света-Сослан
#
# Sample Input 3:
#
# Пермь-Казань-Ижевск-Оренбург
#
# Sample Output 3:
#
# Ижевск-Казань-Оренбург-Пермь

# объявление функции
def print_sorted_hyphen(s):
    word_separator = '-'
    sorted_hyphen = s.split(word_separator)
    sorted_hyphen.sort()
    print(*sorted_hyphen, sep=word_separator)

# считываем данные
s = input()

# вызываем функцию
print_sorted_hyphen(s)
