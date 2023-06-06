# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

m = int(input("Введите количество элементов списка: "))
# # random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
# # n = [random.randint(0, m) for i in range(random.randint(0, m))]

list_m =  [random.randint(-5, m) for x in range(1, m+1)]
print(list_m)

first_index = 0
last_index = m-1

for i in range(len(list_m)):
    if first_index <= list_m[i] <= last_index:

       print(i, end=' ')


