# Вам доступен список словарей users. Напишите программу, которая выводит имена всех пользователей (в алфавитном порядке), чей номер оканчивается на 88.
#
# Примечание 1. Считайте, что список users уже объявлен в вашей программе, и вы имеете к нему доступ.
#
# Примечание 2. Имена необходимо вывести на одной строке, разделяя символом пробела.
#
# Примечание 3. Гарантируется, что имя пользователя присутствует в словаре и доступно по ключу name.
#
# Примечание 4. Гарантируется, что номер пользователя присутствует в словаре и доступен по ключу phone.
#
#  Sample Input 1:
#
# users = [
#     {'name': 'Hank', 'phone': '124-3818', 'email': 'hank@gmail.com'},
#     {'name': 'Petr', 'phone': '555-1618', 'email': 'helga@mail.net'},
#     {'name': 'Sasha', 'phone': '449-3141', 'email': ''},
#     {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#     {
#         'name': 'Maria',
#         'phone': '12-129-3149',
#         'email': 'm.shark@yandex.ru',
#         'city': 'Pskov'
#     },
#     {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#     {
#         'name': 'Tony',
#         'phone': '242-449-3878',
#         'email': 'tony.ggg@mail.ru',
#         'birth_year': 1111
#     },
# ]
#  Sample Output 1:
#
# Hank LJ Petr Tony
#
# Sample Input 2:
#
# users = [
#     {'phone': '120-3518', 'name': 'Mike', 'city': 'Moscow'},
#     {'name': 'Nadya', 'phone': '813-1618', 'city': 'Paris'},
#     {'name': 'Sasha', 'phone': '449-3141', 'email': ''},
#     {'phone': '876-9655', 'name': 'Alexei', 'surname': 'Tolinkov'}
# ]
#
# Sample Output 2:
#
# Mike Nadya

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

result = [user['name'] for user in users if user['phone'].endswith('8')]

print(*sorted(result))
