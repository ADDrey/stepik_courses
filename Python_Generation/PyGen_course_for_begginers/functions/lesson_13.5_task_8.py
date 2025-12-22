# Правильная скобочная последовательность 🌶️
#
# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение True, если поступившая на вход строка является правильной скобочной последовательностью, или False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), где каждой открывающей скобке найдётся парная закрывающая скобка (при этом каждая открывающая скобка должна быть левее соответствующей ей закрывающей скобки).
#
# Примечание 2. Приведённый ниже код:
#
# print(is_correct_bracket('()(()())'))
# print(is_correct_bracket(')(())('))
#
# должен выводить:
#
# True
# False
#
#
#
# Sample Input 1:
#
# ((()))
#
# Sample Output 1:
#
# True
#
# Sample Input 2:
#
# (()())
#
# Sample Output 2:
#
# True
#
# Sample Input 3:
#
# (())()
#
# Sample Output 3:
#
# True


# объявление функции
def is_correct_bracket(text):
    counter = 0
    for i in text:
        if counter < 0:
            return False
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1
    if counter == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))