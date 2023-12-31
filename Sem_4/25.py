# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2



input = 'a a a b c a a d c d d'

text = input.split()
unLetters = {}

for el in text:
    if el in unLetters:
        print(f"{el}_{unLetters[el]}", end = ' ')
        unLetters[el] += 1
    else:
        print(el, end = ' ')
        unLetters[el] = 1