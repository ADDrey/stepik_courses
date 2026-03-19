# Вам доступна строка sentence. Используя генератор множеств, напишите программу, которая создает множество, содержащее уникальные слова (в нижнем регистре) строки sentence длиною меньше 44 символов. Результат выведите на одной строке в алфавитном порядке, разделяя слова одним символом пробела.
#
# Примечание 1. Считайте, что строка sentence уже объявлена в вашей программе, и вы имеете к ней доступ.
#
# Примечание 2. Учтите, что знаки пунктуации :,.!?(); не относятся к словам.
#
#  Sample Input 1:
#
# sentence = 'Dying for the right cause is the most human thing we can do.'
#
# Sample Output 1:
#
# can do for is the we
#
# Sample Input 2:
#
# sentence = 'Очевидно, он вылетел до начала урагана, но первые предвестники его появились еще восемнадцатого марта; следовательно, шар, мчавшийся со скоростью не менее двух тысяч миль в сутки, должен был прилететь из очень далеких краев.'
#
# Sample Output 2:
#
# был в до его еще из не но он со шар

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''


# Очищаем каждое слово от пунктуации, оставляя только буквы
myset = {
    ''.join(char for char in word if char.isalpha()).lower()
    for word in sentence.split()
}

# Удаляем пустые строки и фильтруем по длине (< 4)
myset = {word for word in myset if len(word) > 0 and len(word) < 4}

# Вывод в алфавитном порядке
print(*sorted(myset))