# Задача №11.
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.


# Output: 6 

a = 5
f1 = 0
f2 = 1
f3 = 1
result = 0

while a > f3:
        f3 = f2 + f1
        f1 = f2
        f2 = f3
        result += 1

if a == f3:
    print(result + 2)
else:
    print("-1")

