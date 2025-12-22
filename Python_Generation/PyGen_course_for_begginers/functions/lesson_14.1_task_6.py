# Магические даты ✨
#
# Магическая дата – это дата, когда день, умноженный на месяц, равен числу, образованному последними двумя цифрами года.
#
# Напишите функцию is_magic(date), которая принимает в качестве аргумента строковое представление корректной даты и возвращает значение True, если дата является магической, или False в противном случае.
#
# Примечание. Приведённый ниже код:
#
# print(is_magic('10.06.1960'))
# print(is_magic('11.06.1960'))
#
# должен выводить:
#
# True
# False
#
#
# Sample Input 1:
#
# 10.06.1960
#
# Sample Output 1:
#
# True
#
# Sample Input 2:
#
# 15.03.1945
#
# Sample Output 2:
#
# True

# объявление функции
def is_magic(date):
    list_date = date.split(".")
    if int(list_date[0]) * int(list_date[1]) == int(list_date[2]) % 100:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
