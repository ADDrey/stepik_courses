# Число словами 🌶️
#
# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и возвращает его словесное описание на русском языке.
#
# Примечание 1. Считайте, что число 1≤num≤991≤num≤99.
#
# Примечание 2. Приведённый ниже код:
#
# print(number_to_words(7))
# print(number_to_words(85))
#
# должен выводить:
#
# семь
# восемьдесят пять
#
#
# Sample Input 1:
#
# 1
#
# Sample Output 1:
#
# один
#
# Sample Input 2:
#
# 2
#
# Sample Output 2:
#
# два
#
# Sample Input 3:
#
# 3
#
# Sample Output 3:
#
# три

# объявление функции
def number_to_words(num):
    numbers = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать", 40: "сорок", 90: "девяносто"}

    for key in numbers:
        if num == key:
            return numbers[key]
    if num // 10 in [5, 6, 7, 8] and 1 <= num % 10 <= 9:
        return str(numbers[num // 10]) + "десят " + numbers[num % 10]
    elif num // 10 in [5, 6, 7, 8] and num % 10 == 0:
        return str(numbers[num // 10]) + "десят"
    elif num // 10 * 10 in numbers and 1 <= num % 10 <= 9:
        return str(numbers[num // 10 * 10]) + " " + numbers[num % 10]
    elif num // 10 * 10 in numbers and num % 10 == 0:
        return str(numbers[num // 10 * 10])

    if num in numbers:
        return numbers[num]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))