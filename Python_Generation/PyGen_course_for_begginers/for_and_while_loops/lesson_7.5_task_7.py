# Первый никнейм 👉
#
# У Тимура есть список никнеймов соцсети FriendsGram. Напишите программу, которая выводит первый никнейм, не содержащий символ нижнего подчёркивания _.
#
# Формат входных данных
# На вход программе подаются никнеймы, каждый на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести первый никнейм, не содержащий символ нижнего подчёркивания _.
#
# Примечание. Гарантируется, что хотя бы один никнейм не содержит символ нижнего подчёркивания _.
#
#
# Sample Input 1:
#
# @monica_bing
# @how_you_doing1😎
# @divorce_guy💔
# @richard777
# @rachel_g
#
# Sample Output 1:
#
# @richard777
#
# Sample Input 2:
#
# @emily_geller😈
# @ReginaPhalange😵
#
# Sample Output 2:
#
# @ReginaPhalange😵

underskore_flag = True
while underskore_flag:
    nikname_with_underscore = input()
    underskore_flag = '_' in nikname_with_underscore

print(nikname_with_underscore)
