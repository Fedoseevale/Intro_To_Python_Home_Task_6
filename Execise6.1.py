# Задача 2.3
# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random

my_listSize = int(input('Введите размер списка: '))
my_list = []

# Исходный вариант создания списка:
# for i in range(my_listSize):
#     my_list.append(random.randint(0, 100))
# print(f'Имеется список: {my_list}')

# Вариант создания списка с использованием 'list comprehension'
my_list = [random.randint(0, 100) for i in range(my_listSize)]
print(my_list)
for i in range(my_listSize // 2):
    obj = my_list[i+1]
    my_list[i+1] = my_list[my_listSize - 1 - i]
    my_list[my_listSize - 1 - i] = obj
print(f'Перемешанный список выглядит следующим образом: {my_list}')