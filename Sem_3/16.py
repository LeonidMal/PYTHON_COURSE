# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5                                                 
# 3
# -> 1


import random

elValue = int(input("Введите кол-во элементов в массиве:"))
x = str(round(random.randint(1, elValue)))
numList = str([i for i in range(1, elValue + 1)])

print(f"Проверяемое число - {x}")
print(f"Проверяется в списке - {numList}")
print(numList.count(x))

#                                                    -----------------------------------------------------------------------------------------

# import random

# elValue = int(input("Введите кол-во элементов в массиве:"))
# x = str(round(random.randint(1, elValue)))
# numList = str([i for i in range(1, elValue + 1)])

# testNum = x
# counter = 0

# for i in numList:
#     if i == testNum:
#         counter += 1

# print(f"Проверяемое число - {x}")
# print(f"Проверяется в списке - {numList}")
# print(counter)


