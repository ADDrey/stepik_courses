# Good password 🌶️
#
# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True, если пароль является надёжным, или False в противном случае.
#
# Пароль является надёжным, если:
#
#     его длина не менее 88 символов;
#     он содержит как минимум одну заглавную букву (верхний регистр);
#     он содержит как минимум одну строчную букву (нижний регистр);
#     он содержит хотя бы одну цифру.
#
# Примечание. Приведённый ниже код:
#
# print(is_password_good('aabbCC11OP'))
# print(is_password_good('abC1pu'))
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
# aaAA12qqp
#
# Sample Output 1:
#
# True
#
# Sample Input 2:
#
# aa13AN
#
# Sample Output 2:
#
# False

# объявление функции
def is_password_good(password):
    """ его длина не менее 8 символов;
        он содержит как минимум одну заглавную букву (верхний регистр);
        он содержит как минимум одну строчную букву (нижний регистр);
        он содержит хотя бы одну цифру.
    """
    if len(password) < 8:
        return False
    upper = False
    lower = False
    digit = False
    for i in password:
        if i.isalpha() and i.isupper() and not upper:
            upper = True
        if i.isalpha() and i.islower() and not lower:
            lower = True
        if i.isdigit() and not digit:
            digit = True
    return upper and lower and digit

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
