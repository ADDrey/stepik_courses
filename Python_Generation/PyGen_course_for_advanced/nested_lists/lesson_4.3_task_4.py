# Треугольник Паскаля 2
# 
# На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.
# 
# Формат входных данных
# На вход программе подается число n (n≥1)n(n≥1).
# 
# Формат выходных данных
# Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке, в соответствии с образцом.
# 
# 
# 
# Sample Input 1:
# 
# 4
# 
# Sample Output 1:
# 
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 
# Sample Input 2:
# 
# 5
# 
# Sample Output 2:
# 
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 
# Sample Input 3:
# 
# 2
# 
# Sample Output 3:
# 
# 1
# 1 1

def pascal(str_num: int) -> list:
    if str_num == 0: 
        return [1]
    seq = pascal(str_num - 1)
    pascal_seq_num = [1] + [seq[i] + seq[i + 1] for i in range(len(seq) - 1)] + [1]
    return pascal_seq_num


str_num = int(input())
for i in range(str_num):
    print(*pascal(i))

