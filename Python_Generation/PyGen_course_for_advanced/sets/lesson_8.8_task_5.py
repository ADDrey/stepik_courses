# Используя генератор множеств, напишите программу, которая выбирает из списка files уникальные имена файлов c расширением .png, независимо от регистра имен и расширений. Имена файлов выведите вместе с расширением, все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.
#
# Примечание. Считайте, что список files уже объявлен в вашей программе, и вы имеете к нему доступ.
#
#  Sample Input 1:
#
# files = ['pygen_icon.png', 'Oppenheimer(2024).mkv', 'ideas.TxT', 'codes.txt', 'avatar.PNG']
#
# Sample Output 1:
#
# avatar.png pygen_icon.png
#
# Sample Input 2:
#
# files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
#
# Sample Output 2:
#
# apple.png python.png zebra.png


files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

png_files = {file.lower() for file in files if file.lower().endswith('.png')}

print(*sorted(png_files))
