# Вам доступна строка sentence. Используя генератор множеств, напишите программу, которая создает множество, содержащее уникальные слова (в нижнем регистре) строки sentence. Результат выведите на одной строке в алфавитном порядке, разделяя слова одним символом пробела.
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
# can cause do dying for human is most right the thing we
#
# Sample Input 2:
#
# sentence = 'Очевидно, он вылетел до начала урагана, но первые предвестники его появились еще восемнадцатого марта; следовательно, шар, мчавшийся со скоростью не менее двух тысяч миль в сутки, должен был прилететь из очень далеких краев.'
#
# Sample Output 2:
#
# был в восемнадцатого вылетел далеких двух до должен его еще из краев марта менее миль мчавшийся начала не но он очевидно очень первые появились предвестники прилететь скоростью следовательно со сутки тысяч урагана шар


sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

import string

myset = {word.strip(string.punctuation).lower() for word in sentence.split()}

myset.discard('')
print(*sorted(myset))