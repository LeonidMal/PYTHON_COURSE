





n = 7                                               # ПРОВЕРКА, ЯВЛЯЕТСЯ ЛИ n ПРОСТЫМ ЧИСЛОМ

def simpNum(a, d = 2):
    if a == 2 or d * d > a:
        return 'yes'
    elif a % d == 0:
        return 'no'
    return simpNum(a, d + 1)

print(simpNum(n))