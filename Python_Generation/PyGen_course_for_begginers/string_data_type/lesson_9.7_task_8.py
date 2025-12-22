# Сбой в системе ⚠️🌶️
#
# После недавнего сбоя в операционной системе от компании «Oursoft» у Гвидо сбилась кодировка на компьютере. Теперь все буквы русского алфавита отображаются в некорректном виде:
#
# [u-<номер символа в таблице Unicode>]
#
# Гвидо ещё не научился читать символы в таком формате, поэтому просит вас написать программу, которая будет "расшифровывать" для него все тексты на компьютере.
#
# На вход программе подаётся строка текста. Расшифруйте текст, заменив все конструкции [u-<номер символа в таблице Unicode>] на соответствующие буквы русского алфавита, и выведите его.
#
# Формат входных данных
# На вход программе подаётся строка текста, в которой могут быть зашифрованы символы русского алфавита.
#
# Формат выходных данных
# Программа должна вывести строку текста, расшифровав символы русского алфавита.
#
# Примечание. Будем считать, что буквы Ё нет в русском алфавите. 🤫
#
#
# Sample Input 1:
#
# Hello, my name is [u-1061][u-1072][u-1082][u-1080]!
#
# Sample Output 1:
#
# Hello, my name is Хаки!
#
# Sample Input 2:
#
# Username: [u-1042][u-1072][u-1089][u-1103]; City: [u-1050][u-1072][u-1079][u-1072][u-1085][u-1100]
#
# Sample Output 2:
#
# Username: Вася; City: Казань
#
# Sample Input 3:
#
# Because I didn't know what I had until it was gone! All right?
#
# Sample Output 3:
#
# Because I didn't know what I had until it was gone! All right?


message = input()

while message.find('[u-') != -1:
    first_letter_id = message.find('[u-')+3
    end_letter_id = first_letter_id+4
    char_id = message[first_letter_id: end_letter_id]
    letter = chr(int(char_id))
    message = message.replace(f"[u-{char_id}]", letter)

print(message)
