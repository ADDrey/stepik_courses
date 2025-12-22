# Палиндром
#
# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True, если указанный текст является палиндромом, или False в противном случае.
#
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
#
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы и символы ,.!?-.
#
# Примечание 3. Приведённый ниже код:
#
# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby - burrel bag!'))
# print(is_palindrome('BEEGEEK'))
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
# Standart - smallest, sell Amstrad nats.
#
# Sample Output 1:
#
# True
#
# Sample Input 2:
#
# Zoo belt to be Russia, is sure bottle booz.
#
# Sample Output 2:
#
# True

def is_palindrome(text):
    only_text = text.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("-", "")
    reversed_text = ''.join(reversed(only_text))
    if only_text == reversed_text:
        return True
    return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
