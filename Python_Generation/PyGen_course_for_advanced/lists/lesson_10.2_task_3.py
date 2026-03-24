# Вам доступен список словарей users. Напишите программу, которая выводит имена всех пользователей (в алфавитном порядке), у которых нет информации об электронной почте.
#
# Примечание 1. Считайте, что список users уже объявлен в вашей программе, и вы имеете к нему доступ.
#
# Примечание 2. Имена необходимо вывести на одной строке, разделяя символом пробела.
#
# Примечание 3. Гарантируется, что имя пользователя присутствует в словаре и доступно по ключу name.
#
# Примечание 4. Ключ email может отсутствовать в словаре.
#
#  Sample Input 1:
#
# users = [
#     {'name': 'Andrew', 'email': 'and@gmail.com'},
#     {'name': 'Tim', 'phone': '555-1618', 'email': 'tim-tim@yandex.ru'},
#     {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#     {'name': 'Vika', 'phone': '547-2123', 'email': 'Viko4ka@gmail.com'},
#     {'name': 'Kate', 'surname': 'Maltseva', 'city': 'Vologda'},
# ]
#
# Sample Output 1:
#
# Kate Olivia
#
# Sample Input 2:
#
# users = [
#     {'name': 'Viktor', 'phone': '547-2123'},
#     {'name': 'dasha', 'email': 'dasha75@yandex.ru'},
#     {'name': 'John', 'phone': '555-1875', 'email': 'tim-tim@yandex.ru'},
#     {'name': 'Olivia', 'phone': '449-3141', 'email': 'oliv@mail.ru'},
#     {'name': 'Anna', 'city': 'Hawkins', 'email': 'demo-dog@gmail.com'}
# ]
#
# Sample Output 2:
#
# Viktor


users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

no_email_users = [user['name'] for user in users if 'email' not in user or user['email'] == '']
no_email_users.sort()
print(*no_email_users)
