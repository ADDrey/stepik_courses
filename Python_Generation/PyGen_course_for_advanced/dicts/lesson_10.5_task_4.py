# В чем отличие ❓
#
# Напишите функцию dict_diff(), которая принимает два аргумента в следующем порядке:
#
#     data1 – первый словарь
#     data2 – второй словарь
#
# Функция должна возвращать словарь – результат сравнения словаря data1 относительно словаря data2. В результирующем словаре ключами будут ключи из переданных словарей, а значениями – строки с описанием отличий:
#
#     'added' – ключ отсутствует в первом словаре и присутствует во втором
#     'deleted' – ключ присутствует в первом словаре и отсутствует во втором
#     'changed' – ключ присутствует и в первом, и во втором словарях, но значения отличаются
#     'unchanged' – ключ и значение находятся без изменений и в первом, и во втором словарях
#
# Примечание 1. Порядок элементов в результирующем словаре не учитывается.
#
# Примечание 2. Вызывать функцию dict_diff() не нужно, требуется только реализовать ее.
#
# Входные данные
# data1 = {'one': 1, 'two': 2, 'four': 4}
# data2 = {'two': 2.5, 'three': 3, 'four': 4}
# print(dict_diff(data1, data2))
#
# Выходные данные
# {'one': 'deleted', 'two': 'changed', 'four': 'unchanged', 'three': 'added'}
#

def dict_diff(data1, data2):
    all_keys = set(data1) | set(data2)
    result = {}

    for key in all_keys:
        in1 = key in data1
        in2 = key in data2

        if in1 and in2:
            if data1[key] == data2[key]:
                result[key] = 'unchanged'
            else:
                result[key] = 'changed'
        elif in1 and not in2:
            result[key] = 'deleted'
        elif not in1 and in2:
            result[key] = 'added'

    return result