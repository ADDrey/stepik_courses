# Звёздный треугольник ⭐
#
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
#     fill – символ заполнитель;
#     base – величина основания равнобедренного треугольника;
#
# а затем выводит его.
#
# Примечание. Гарантируется, что основание треугольника – нечётное число.
#
#
# Sample Input 1:
#
# *
# 9
#
# Sample Output 1:
#
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
#
# Sample Input 2:
#
# +
# 5
#
# Sample Output 2:
#
# +
# ++
# +++
# ++
# +
#
# Sample Input 3:
#
# ?
# 7
#
# Sample Output 3:
#
# ?
# ??
# ???
# ????
# ???
# ??
# ?

# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        if i <= base // 2 + 1:
            print(fill * i)
        else:
            print(fill * (base - i + 1))

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
