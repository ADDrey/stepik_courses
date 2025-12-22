# Последнее вхождение 🔚
#
# Напишите функцию get_last_index(data, value), которая принимает на вход список data и некоторое значение value и возвращает индекс последнего вхождения данного значения в список или текст «ERROR!» (без кавычек), если искомое значение отсутствует в списке.
#
# Примечание 1. Если искомое значение встречается в списке только один раз, то нужно вернуть индекс этого вхождения.
#
# Примечание 2. Приведённый ниже код:
#
# print(get_last_index(['🦆', '🐝', '🐍', '🐍', '🐝'], '🐝'))
# print(get_last_index(['Ross', 'Joey', 'Mike'], 'Ross'))
# print(get_last_index(['синий', 'белый', 'фиолетовый'], 'красный'))
#
# должен выводить:
#
# 4
# 0
# ERROR!
#
# Примечание 3. Обратите внимание на то, что для принятия данных на вход в программе используется функция eval(). На текущем этапе обучения не нужно разбираться в её устройстве: данная функция изучается подробно в нашем курсе для профессионалов.
#
#
# Sample Input 1:
#
# ['Валера', 'Тимур', 'Артур', 'Света', 'Сослан', 'Артур', 'Антон']
# 'Артур'
#
# Sample Output 1:
#
# 5
#
# Sample Input 2:
#
# [4, 9, -4, 2, 3, 1, 1]
# 1
#
# Sample Output 2:
#
# 6
#
# Sample Input 3:
#
# ['uno', 'uno', 'uno', 'un', 'momento']
# 'uno'
#
# Sample Output 3:
#
# 2

# объявление функции
def get_last_index(data, value):
    if value in data and data.count(value) == 1:
        last_index = data.index(value)
        return last_index
    elif value in data:
        last_index = data.index(value)
        value_count = data.count(value) - 1  # Одно вхождение учитывается выше
        while value_count:
            last_index = data.index(value, last_index + 1)
            value_count -= 1
        return last_index
    else:
        return 'ERROR!'

# считываем данные
data = eval(input())
value = eval(input())

# вызываем функцию
print(get_last_index(data, value))
