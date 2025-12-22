# Панграммы 🌶️
#
# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.
#
# Напишите функцию is_pangram(text), которая принимает в качестве аргумента строку текста на английском языке и возвращает значение True, если текст является панграммой, или False в противном случае.
#
# Примечание 1. Гарантируется, что введённая строка содержит только буквы английского алфавита и пробелы.
#
# Примечание 2. Приведённый ниже код:
#
# print(is_pangram('Jackdaws love my big sphinx of quartz'))
# print(is_pangram('The jay pig fox zebra and my wolves quack'))
# print(is_pangram('Hello world'))
#
# должен выводить:
#
# True
# True
# False
#
#
# Sample Input 1:
#
# Jackdaws love my big sphinx of quartz
#
# Sample Output 1:
#
# True
#
# Sample Input 2:
#
# The five boxing wizards jump quickly
#
# Sample Output 2:
#
# True

# объявление функции
def is_pangram(text):
    lower_text = text.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in alphabet:
        if i not in lower_text:
            return False
    return True
# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
