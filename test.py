# n = 423                                                                 # НАХОЖДЕНИЕ СУММЫ ЧИСЕЛ ТРЁХЗНААЧНОГО ЧИСЛА
# summa = 0
# while n > 0:
#     x = n % 10
#     summa += x
#     n //= 10
# print (summa)

#--------------------------------------------------------------------------------------------------------------------------------------------



# t = [1, 'hello', "chiao", True]                                        # СПИСОК ДУБЛИРУЕТ САМ СЕБЯ
# for i in range(len(t)):
#     t.append(t[i])
#     print(t)

#--------------------------------------------------------------------------------------------------------------------------------------------



# array = [2,2,2,2,2]                                                    # ПЕРЕЗАПИСЬ СПИСКА
# for i in range(len(array)):
#     array[i] = 5
# print(array)

#--------------------------------------------------------------------------------------------------------------------------------------------



# list =  [1, 2, 3, 4, 5]                                                # СДВИГ ВСЕЙ ПОСЛЕДОВАТЕЛЬНОСТИ НА "k" ЭЛЕМЕНТОВ ВПРАВО
# k = 3

# for i in range(k):
#     temp = list[-1]
#     for j in range(len(list) - 1):
#         list[-j - 1] = list[-j - 2]
#     list[0] = temp
# print(list)
#-----------------------------------------------------------------------

#list =  [1, 2, 3, 4, 5]                                                # СДВИГ ВСЕЙ ПОСЛЕДОВАТЕЛЬНОСТИ НА "k" ЭЛЕМЕНТОВ ВПРАВО
# k = 3

# list = [i for i in range(1, int(input("Количество чисел: ")) + 1)]       
# k = int(input("Сдвиг на "))
# print()

# for i in range(k):
#     temp_list = [list[-1],]
#     for j in range(len(list) - 1):
#         temp_list.append(list[j])
#     list = temp_list
# print(list)

#--------------------------------------------------------------------

# list =  [1, 2, 3, 4, 5]                                                # СДВИГ ВСЕЙ ПОСЛЕДОВАТЕЛЬНОСТИ НА "k" ЭЛЕМЕНТОВ ВПРАВО
# k = 3

# for i in range(k): 
#     list.insert(0, list.pop())

# print(list)

#--------------------------------------------------------------------------------------------------------------------------------------------



# list = [1, 1, 1, 2, 0, -2, 5, 5, 5, 5, 1, -2, -1, 3, 4, 4, 2]         # ОЧИСТКА СПИСКА ОТ ПОВТОРЯЮЩИХСЯ ЗНАЧЕНИЙ (ПОИСК УНИКАЛЬНЫХ ЗНАЧЕНИЙ СПИСКА)
# newList = [list[0]]
# t = 1
# counter = 0

# for t in list:
#     for i in range(len(newList)):
#         if newList[i] != t:
#             counter += 1
#     if counter == len(newList):
#         newList.append(t)
#     counter = 0

# print(len(newList))
# print(newList)

#----------------------------------------------------------------

# list = [1, 1, 1, 2, 0, -2, 5, 5, 5, 5, 1, -2, -1, 3, 4, 4, 2]         # ОЧИСТКА СПИСКА ОТ ПОВТОРЯЮЩИХСЯ ЗНАЧЕНИЙ (ПОИСК УНИКАЛЬНЫХ ЗНАЧЕНИЙ СПИСКА)
# newList = [list[0]]

# for i in list:
#     if i not in newList:
#         newList.append(i)

# print(len(newList))

#--------------------------------------------------------------------------------------------------------------------------------------------



# list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},                         # ВЫВОД ВСЕХ УНИКАЛЬНЫХ ЧИСЕЛ ИЗ СПИСКА СЛОВАРЕЙ
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# newList = []

# for i in list:
#         for j in i.values():
#             newList.append(j.strip())
# print(set(newList))

#----------------------------------------------------------------

# list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},                         # ВЫВОД ВСЕХ УНИКАЛЬНЫХ ЧИСЕЛ ИЗ СПИСКА СЛОВАРЕЙ
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# newList = []

# for j in list:
#     newList += [i.strip() for i in j.values()]

# print(set(newList))

#--------------------------------------------------------------------------------------------------------------------------------------------



# list = [-2, -1, 0, -1, 5, 1000, 1, 2, 3]                                        # ПОДСЧЁТ КОЛИЧЕСТВА ЭЛЕМЕНТОВ МАССИВА, БОЛЬШИХ ПРЕДЫДУЩЕГО
# counter = 0

# for i in range(len(list) - 1):
#     if list[i + 1] > list[i]:
#         counter += 1

# print(counter)

#--------------------------------------------------------------------------------------------------------------------------------------------



# input = 'a a a b c a a d c d d'                             # ОТСЛЕЖМВАНИЕ, СКОЛЬКО РАЗ КАЖДЫЙ СИМВОЛ ВСТРЕЧАЕТСЯ В СТРОКЕ И ДОБАВЛЕНИЕ '_N'

# text = input.split()
# unLetters = {}

# for el in text:
#     if el in unLetters:
#         print(f"{el}_{unLetters[el]}", end = ' ')
#         unLetters[el] += 1
#     else:
#         print(el, end = ' ')
#         unLetters[el] = 1

#--------------------------------------------------------------------------------------------------------------------------------------------



# var1 = '1 4'                                                  # ВЫВОД СОВПАДАЮЩИХ ЭЛЕМЕНТОВ ДВУХ МНОЖЕСТВ В ПОРЯДКЕ ВОЗРАСТАНИЯ
# var2 = '1'
# var3 = '3 4 5 6'

# textList = var1.split()
# multi_1 = set(var2.split())
# multi_2 = set(var3.split())
# multi = multi_1.intersection(multi_2)
# result = list(multi)
# result.sort()

# for i in result:
#     print(i, end = ' ')

# ---------------------------------------------------------------

# textList = input("Введите числа через пробел").split()
# multi = set()
# print(textList)

# for i in textList:
#     for j in range(int(i)):
#         multi.add(input("Введите элемент(число)"))

# multi = list(multi)
# multi.sort()

# print(multi)

#--------------------------------------------------------------------------------------------------------------------------------------------

 

# a = 3                                                          # ВОЗВЕДЕНИЕ ЧИСЛА a В ЦЕЛУЮ СТЕПЕНЬ b С ПОМОЩЬЮ РЕКУРСИИ
# b = 5

# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a

# print(f(a, b))

# ---------------------------------------------------------------

# a = 3
# b = 5

# def f(n, m, q = 1):
#     if m < 1:
#         n = q
#         return n
#     q = q * n
#     return f(n, m - 1, q)

# print(f(a, b))

# -------------------------------------------------------------------------------------------------------------------------------------------


# На выходе:                                                     # СОСТАВЛЕНИЕ ТАБЛИЦЫ АРИФМЕТИЧЕСКОГО ДЕЙСТВИЯ (*, +, -, /)

# 1 2 3
# 2 4 6 
# 3 6 9


# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         header = ' '.join([str(i) for i in range(1, num_columns + 1)])
#         print(header)
#         for i in range(2, num_rows + 1):
#             row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
#             print(' '.join(row))

# print_operation_table(lambda x, y: x + y, 4, 4)

# ---------------------------------------------------------------

# def print_operation_table(operation, num_rows, num_columns):
#     list_rows = [i for i in range(1, num_rows + 1)]
#     list_columns = [i for i in range(2, num_columns + 1)]
#     nums = [i for i in list_rows]

#     if num_rows > 2:
#         for i in list_columns:
#             nums.append(i)
#             for j in range(len(list_rows) - 1):
#                 nums.append(operation(i, list_rows[j + 1]))

#         for p in range(len(nums)):
#                 counter = p + 1
#                 print(nums[p], end =' ')
#                 if counter % num_columns == 0:
#                     print()
#     else:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')

# print_operation_table(lambda x, y: x + y, 4, 4)

# -------------------------------------------------------------------------------------------------------------------------------------------



# count = 0                    =
# for l in stroka[i]:          =
#     if l in glasnye:         =        countGlasnye.append(len([l for l in stroka[i] if l in glasnye]))
#         count += 1           =
# countGlasnye.append(count)   =

# -------------------------------------------------------------------------------------------------------------------------------------------



