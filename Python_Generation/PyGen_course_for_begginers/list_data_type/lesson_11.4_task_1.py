# Дополните приведённый ниже код так, чтобы он вывел сумму квадратов элементов списка numbers.
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
summary = 0
for num in numbers:
    summary += num ** 2
print(summary)
