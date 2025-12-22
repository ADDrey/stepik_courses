# Интересное число 🤔
# 
# Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет, интересное число или нет. Если число интересное, следует вывести текст «Число интересное» (без кавычек), иначе – «Число неинтересное» (без кавычек).
# 
# Формат входных данных
# На вход программе подаётся натуральное трёхзначное число.
# 
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
# 
# 
# Sample Input 1:
# 
# 945
# 
# Sample Output 1:
# 
# Число интересное
# 
# Sample Input 2:
# 
# 123
# 
# Sample Output 2:
# 
# Число интересное
# 
# Sample Input 3:
# 
# 896
# 
# Sample Output 3:
# 
# Число неинтересное

value = int(input())
first_num = value // 100
second_num = value % 100 // 10
last_num = value % 10
middle_num = 0

if first_num == min(first_num, second_num, last_num) and second_num == max(first_num, second_num, last_num) or second_num == min(first_num, second_num, last_num) and first_num == max(first_num, second_num, last_num):
    middle_num = last_num
elif first_num == min(first_num, second_num, last_num) and last_num == max(first_num, second_num, last_num) or last_num == min(first_num, second_num, last_num) and first_num == max(first_num, second_num, last_num):
    middle_num = second_num
else:
    middle_num = first_num

if max(first_num, second_num, last_num) - min(first_num, second_num, last_num) == middle_num:
    print("Число интересное")
else:
    print("Число неинтересное")

