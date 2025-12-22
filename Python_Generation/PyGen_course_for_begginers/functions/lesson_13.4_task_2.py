# </code>
#
# Напишите функцию code_format(text), которая принимает строку текста text, оборачивает её в теги <code></code> и возвращает результат.
#
# Примечание 1. Приведённый ниже код:
#
# print(code_format('s = input()'))
# print(code_format('15'))
# print(code_format('None'))
#
# должен выводить:
#
# <code>s = input()</code>
# <code>15</code>
# <code>None</code>
#
# Примечание 2. Во многих тестовых задачах мы обёртываем варианты ответа именно в теги <code></code>.
#
#
# Sample Input 1:
#
# print('Hello, world!')
#
# Sample Output 1:
#
# <code>print('Hello, world!')</code>
#
# Sample Input 2:
#
# name = BEEGEEK🐝
#
# Sample Output 2:
#
# <code>name = BEEGEEK🐝</code>
#
# Sample Input 3:
#
# python3.12
#
# Sample Output 3:
#
# <code>python3.12</code>

# объявление функции
def code_format(text):
    decorated_text = f'<code>{text}</code>'
    return decorated_text

# считываем данные
text = input()

# вызываем функцию
print(code_format(text))
