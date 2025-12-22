# Три города 🏙️
#
# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
#
# Формат входных данных
# На вход программе подаются названия трёх городов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
#
# Примечание. Гарантируется, что длины названий всех трёх городов различны.
#
#
# Sample Input 1:
#
# Москва
# Санкт-Петербург
# Екатеринбург
#
# Sample Output 1:
#
# Москва
# Санкт-Петербург
#
# Sample Input 2:
#
# Нью-Йорк
# Вашингтон
# Чикаго
#
# Sample Output 2:
#
# Чикаго
# Вашингтон
#
# Sample Input 3:
#
# Париж
# Марсель
# Лион
#
# Sample Output 3:
#
# Лион
# Марсель

city1, city2, city3 = input(), input(), input()
if len(city1) == min(len(city1), len(city2), len(city3)):
    print(city1)
elif len(city2) == min(len(city1), len(city2), len(city3)):
    print(city2)
else:
    print(city3)
if len(city1) == max(len(city1), len(city2), len(city3)):
    print(city1)
elif len(city2) == max(len(city1), len(city2), len(city3)):
    print(city2)
else:
    print(city3)