# Напишите функцию greet(), которая принимает произвольное количество строк-имен (как минимум одну) и возвращает приветствие в соответствии с тестовыми данными.
#
# Примечание 1. Обратите внимание: функция должна принимать не список, а именно произвольное количество аргументов.
#
# Примечание 2. Вызывать функцию greet() не нужно, требуется только реализовать ее.
#
# Номер
# теста
# Входные
# данные
# Выходные
# данные
# 1
#
# print(greet('Timur'))
#
# Hello, Timur!
#
#
#
#
# 2
#
# print(greet('Timur', 'Roman'))
#
# Hello, Timur and Roman!
#
#
#
#
# 3
#
# print(greet('Timur', 'Roman', 'Ruslan'))
#
# Hello, Timur and Roman and Ruslan!
#
#
#
#
# 4
#
# print(greet('Soltan'))
#
# Hello, Soltan!
#
#
#
#
# 5
#
# print(greet('Madlen', 'Tom', 'Tim', 'Jerry', 'Donald', 'Alina'))
#
# Hello, Madlen and Tom and Tim and Jerry and Donald and Alina!

def greet(*names):
    if len(names) == 1:
        return f"Hello, {names[0]}!"
    else:
        return f"Hello, {' and '.join(names)}!"
