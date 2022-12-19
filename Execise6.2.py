# Задача 3.3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

size = int(input('Введите размер списка: '))

# Старый вариант
# my_Bestlist = []
# for i in range(size):
#     my_Bestlist.append(round(random.uniform(0, 100), 2))
# print(f'Имеется список: {my_Bestlist}')

# Вариант с использованием 'list comprehension'
my_Bestlist = []
my_Bestlist = [round(random.uniform(0, 100), 2) for i in range(size)]
print(f'Имеется список: {my_Bestlist}')

def listDiffMinNumMaxNum (my_list):
    # Прежний вариант
    # for i in range(len(my_list)):
    #     my_list[i] = str(my_list[i])
    #     my_list[i] = my_list[i].split('.')
    # print(my_list)

    # Вариант с использованием функции 'map'
    my_list = list(map(str, my_list))
    for i in range(len(my_list)):
        my_list[i] = my_list[i].split('.')
    # print(my_list)

    my_list2 = []
    for i in range(len(my_list)):
        if len(my_list[i]) > 1:
            my_list2.append(my_list[i])
    # print(my_list2)

    my_list3 = []
    for i in range(len(my_list2)):
        my_list3.append(my_list2[i][1])
    # print(my_list3)

    for i in range(len(my_list3)):
        if len(my_list3[i]) == 1:
            my_list3[i] = my_list3[i] + '0'
    # print(my_list3)

    for i in range(len(my_list3)):
        my_list3[i] = float(my_list3[i])
        my_list3[i] = my_list3[i] / 100
    # print(my_list3)

    maxNum = max(my_list3)
    # print(maxNum)
    minNum = min(my_list3)
    # print(minNum)
    diffMinNumMaxNum = round((maxNum - minNum), 2)
    # print(diffMinNumMaxNum)
    return(diffMinNumMaxNum)

my_diffMinNumMaxNum = listDiffMinNumMaxNum(my_Bestlist)
print(f'Разница между максимальным и минимальным значением дробной части элементов данного списка '
      f'равна {my_diffMinNumMaxNum}')