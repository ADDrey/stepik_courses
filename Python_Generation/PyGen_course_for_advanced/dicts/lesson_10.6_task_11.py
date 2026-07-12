# Вам доступны три списка student_ids, student_names, student_grades, содержащие идентификаторы, имена и оценки студентов соответственно. Используя генератор словарей, напишите программу, которая выводит список, содержащий вложенные словари в следующем виде:
#
# {<идентификатор>: {<имя>: <оценка>}}
#
# Примечание 1. Считайте, что списки student_ids, student_names, student_grades уже объявлены в вашей программе, и вы имеете к ним доступ.
#
# Примечание 2. Для параллельной итерации по всем трем спискам одновременно можно использовать встроенную функцию zip().
#
#
#  Sample Input 1:
#
# student_ids = ['X142', 'B065', 'X144']
# student_names = ['Nikita Karpov', 'Anna Chernova', 'Ruslan Magarov']
# student_grades = [88, 85, 62]
#
# Sample Output 1:
#
# [
#     {'X142': {'Nikita Karpov': 88}}, {'B065': {'Anna Chernova': 85}},
#     {'X144': {'Ruslan Magarov': 62}},
# ]
#
# Sample Input 2:
#
# student_ids = ['P042', 'A007', 'A742', 'L331', 'V241']
# student_names = [
#     'Viktor Karasev', 'Sasha Chernov', 'Liza Odintsova', 'Petr Ulrikh', 'Anna Vasileva'
# ]
# student_grades = [58, 96, 49, 85, 61]
#
# Sample Output 2:
#
# [
#     {'P042': {'Viktor Karasev': 58}}, {'A007': {'Sasha Chernov': 96}},
#     {'A742': {'Liza Odintsova': 49}}, {'L331': {'Petr Ulrikh': 85}},
#     {'V241': {'Anna Vasileva': 61}},
# ]


result = [
    {student_ids[i]: {student_names[i]: student_grades[i]}}
    for i in range(len(student_ids))
]
print(result)