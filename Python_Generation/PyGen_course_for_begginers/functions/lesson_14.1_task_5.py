# Искомый месяц 📅
#
# Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en и number – номер месяца (от 11 до 1212 включительно) и возвращает название месяца на русском или английском языке.
#
# Примечание. Приведённый ниже код:
#
# print(get_month('ru', 1))
# print(get_month('ru', 12))
# print(get_month('en', 1))
# print(get_month('en', 10))
#
# должен выводить:
#
# январь
# декабрь
# january
# october
#
#
# Sample Input 1:
#
# ru
# 1
#
# Sample Output 1:
#
# январь
#
# Sample Input 2:
#
# ru
# 2
#
# Sample Output 2:
#
# февраль

# объявление функции
def get_month(language, number):
    ru_months = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
    en_months = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

    if language == "en":
        return en_months[number]
    elif language == "ru":
        return ru_months[number]
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
