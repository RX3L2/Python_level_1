# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

print('Задание - 1')
list_input = [random.randint(-10, 10) for _ in range(20)]
list_output = [j ** 2 for j in list_input]
print(list_input)
print(list_output)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('Задание - 2')
list_1 = ['Яблоко', 'Киви', 'Банан', 'Апельсин', 'Манго']
list_2 = ['Дыня', 'Груша', 'Киви', 'Слива', 'Апельсин', 'Абрикос', 'Яблоко']
result = [fruit for fruit in list_1 if list_2.count(fruit) >= 1]
print(result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('Задание - 3')
number_list = [83, 97, -70, -23, -70, -58, 51, -64, 34, -43, 57, -11, 43, -6, -38, 94, 96, -51, 87, -43, 120]
result_list = [x for x in number_list if x / 3 == x // 3 and x > 0 and x / 4 != x // 4]
print(number_list)
print(result_list)
