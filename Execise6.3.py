# Задача 3.1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка
# с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
from functools import reduce

size = int(input('Введите размер списка: '))
my_list = []
# Старый вариант
# for i in range(size):
#     my_list.append(random.randint(0, 10))
# print(f'Имеется список: {my_list}')
#
# sumElWithOddIndexes = 0
# for i in range(1, size, 2):
#     sumElWithOddIndexes += my_list[i]
# print(f'Сумма элементов списка с нечетными индексами равна {sumElWithOddIndexes}')

# Новый вариант с использованием 'list comprehension' и 'lambda':
my_list = [random.randint(0, 100) for i in range(size)]
print(f'Имеется список: {my_list}')

for i in range(0, size, 2):
    my_list.pop(i)
    my_list.insert(i, 0)
# print(my_list)

sumElWithOddIndexes = reduce((lambda x, y: x + y), my_list)
print(sumElWithOddIndexes)