# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

a = int(input('сколько учеников в первом классе?'))
b = int(input('сколько учеников в втором классе?'))
c = int(input('сколько учеников в третьем классе?'))

print(f"понадобится {(a % 2 + a // 2 + (b % 2 > 0) + b // 2 + (c+1) // 2)} парт")

# i = a + b + c                  //не верно - изначально подсчитывается общее кол-во учеников,
# count = 0                        что приводит к подсаживанию двух учеников с разных классов за одну парту                         
                                   
# for i in a, b, c:
#     while i > 0:
#         count += 1
#         i -= 2

# print(count)