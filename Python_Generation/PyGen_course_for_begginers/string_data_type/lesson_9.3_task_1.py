# Заглавные буквы 🔠
#
# На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом. Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
#
# Формат входных данных
# На вход программе подаётся строка.
#
# Формат выходных данных
# Программа должна вывести «YES» (без кавычек), если имя и фамилия начинаются с заглавной буквы, или «NO» (без кавычек) в противном случае.
#
# Примечание. Строка содержит только буквы и символ пробела.
#
#
# Sample Input 1:
#
# chris alan
#
# Sample Output 1:
#
# NO
#
# Sample Input 2:
#
# Chris Alan
#
# Sample Output 2:
#
# YES
#
# Sample Input 3:
#
# chris Alan
#
# Sample Output 3:
#
# NO

user_name = input()

if len(user_name) == 0 or not user_name.find(" "):
    print("NO")
else:
    first_name_symbol = user_name[0]
    first_surname_symbol = user_name[user_name.find(" ") + 1]

    if first_name_symbol.isupper() and first_surname_symbol.isupper():
        print("YES")
    else:
        print("NO")
