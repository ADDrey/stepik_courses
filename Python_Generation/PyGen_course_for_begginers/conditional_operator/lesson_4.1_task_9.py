# Наименьшее из четырёх чисел 🌶️
# 
# Напишите программу, которая определяет наименьшее из четырёх чисел.
# 
# Формат входных данных
# На вход программе подаются четыре целых числа.
# 
# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.
# 
# Примечание. Учитывайте, что минимальные числа могут повторяться (смотрите тест №5). В таком случае необходимо вывести только одно из них.
# 
# 
# Sample Input 1:
# 
# 1
# 2
# 3
# 4
# 
# Sample Output 1:
# 
# 1
# 
# Sample Input 2:
# 
# 10
# 9
# 11
# 12
# 
# Sample Output 2:
# 
# 9
# 
# Sample Input 3:
# 
# 100
# 200
# 5
# 300
# 
# Sample Output 3:
# 
# 5

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b:
    if a < c:
        if a < d:
            print(a)
        else:
            print(d)
    else:
        if c < d:
            print(c)
        else:
            print(d)
else:
    if b < c:
        if b < d:
            print(b)
        else:
            print(d)
    else:
        if c < d:
            print(c)
        else:
            print(d)

