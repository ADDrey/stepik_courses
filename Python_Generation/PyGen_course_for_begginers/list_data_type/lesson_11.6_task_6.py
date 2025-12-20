# Сортируем песни 🎵
#
# На вход программе подаются число nn, а затем – nn песен из плейлиста Сэма, каждая на отдельной строке. Напишите программу, которая сортирует эти песни в алфавитном порядке и выводит каждую из них на отдельной строке.
#
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем – nn строк.
#
# Формат выходных данных
# Программа должна вывести nn песен, отсортированных в алфавитном порядке, каждую на отдельной строке.
#
#
# Sample Input:
#
# 5
# Adele – Skyfall
# Il Volo – Canzone per te
# Timothée Chalamet – Pure Imagination
# Drew Sarich – Gethsemane (I Only Want To Say)
# Il Volo – Grande Amore
#
# Sample Output:
#
# Adele – Skyfall
# Drew Sarich – Gethsemane (I Only Want To Say)
# Il Volo – Canzone per te
# Il Volo – Grande Amore
# Timothée Chalamet – Pure Imagination
#

songs_counter = int(input())
songs = [input() for _ in range(songs_counter)]
songs.sort()
print(*songs, sep='\n')
