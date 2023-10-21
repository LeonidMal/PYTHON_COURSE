# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

elValue = int(input("Введите кол-во элементов в массиве:"))
x = random.randint(1, elValue)
numList = [random.randint(1, elValue) for i in range(elValue)]
value = elValue

for i in numList:
    if x != i and abs(x - i) < value:
        print(f"if выполнено {i}")
        value = abs(x - i)
        number = i
    print(f"value = {value}")
    print("переход наследуюзий for")

print(f" x = {x}")
print(numList)
print(f"number = {number}")