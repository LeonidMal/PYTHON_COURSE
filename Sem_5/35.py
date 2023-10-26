# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes 
n = 7

def simpNum(a, d = 2):
    if a == 2 or d * d > a:
        return 'yes'
    elif a % d == 0:
        return 'no'
    return simpNum(a, d + 1)

print(simpNum(n))