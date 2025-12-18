# .com or .ru 🌐
#
# На вход программе подаётся строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
#
# Формат входных данных
# На вход программе подаётся строка текста.
#
# Формат выходных данных
# Программа должна вывести «YES» (без кавычек), если введённая строка заканчивается подстрокой .com или .ru, или «NO» (без кавычек) в противном случае.
#
#
# Sample Input 1:
#
# www.stepik.org
#
# Sample Output 1:
#
# NO
#
# Sample Input 2:
#
# www.google.com
#
# Sample Output 2:
#
# YES
#
# Sample Input 3:
#
# www.yandex.ru
#
# Sample Output 3:
#
# YES

s = input()
if s.endswith(".ru") or s.endswith(".com"):
    print("YES")
else:
    print("NO")
