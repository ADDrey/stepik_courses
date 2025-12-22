# Ровно в одном 1️⃣
#
# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2. Функция должна возвращать значение True, если слова имеют одинаковую длину и отличаются одним символом на одной и той же позиции, или False в противном случае.
#
# Примечание. Приведённый ниже код:
#
# print(is_one_away('bike', 'hike'))
# print(is_one_away('water', 'wafer'))
# print(is_one_away('abcd', 'abpo'))
# print(is_one_away('abcd', 'abcde'))
#
# должен выводить:
#
# True
# True
# False
# False
#
#
# Sample Input 1:
#
# bike
# hike
#
# Sample Output 1:
#
# True
#
# Sample Input 2:
#
# water
# wafer
#
# Sample Output 2:
#
# True

# объявление функции
def is_one_away(word1, word2):
    differents = 0
    if word1 == word2:
        return False
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differents += 1
        if differents >= 2:
            return False
        else:
            return True
    else:
        return False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
