# Вам доступен список words. Используя генератор множеств, напишите программу, которая создает множество, содержащее первую букву каждого слова (в нижнем регистре) списка words. Результат выведите на одной строке в алфавитном порядке, разделяя буквы одним символом пробела.
#
# Примечание. Считайте, что список words уже объявлен в вашей программе, и вы имеете к нему доступ.
#
#  Sample Input 1:
#
# words = ['summer', 'city', 'Earth', 'peace', 'kindness', 'Dog', 'turtle']
#
# Sample Output 1:
#
# c d e k p s t
#
# Sample Input 2:
#
# words = ['weak', 'Python', 'force', 'knee', 'Harry']
#
# Sample Output 2:
#
# f h k p w

words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']

result = {i[0].lower() for i in words}

print(*sorted(result))