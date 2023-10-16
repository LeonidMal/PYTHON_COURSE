n = 423                 # нахождение суммы цифр трехзначного числа
summa = 0
while n > 0:
    x = n % 10
    summa += x
    n //= 10
print (summa)

# n = range(0, -5, -2)

# for i in n:
#     print(i)