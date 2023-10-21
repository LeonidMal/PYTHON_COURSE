# Задача №9.
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while


# Input: 5
# Output: 120

n = 5
result = 1

if n != 0:
    while 1 < n:
        result = result * n
        n -= 1
else:
    result = 1

print(result) 
