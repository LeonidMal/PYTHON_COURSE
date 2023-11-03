# Задача №51.
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод:                                     Вывод:
# values = [0, 2, 10, 6]                    same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)



values = [0, 2, 10, 6]

def same_by(characteristic, objects):
    if objects != []:
        notCount = 0
        count = 0
        for i in objects:
            if not characteristic(i):
                notCount += 1
            elif characteristic(i):
                count += 1
        if count == len(objects) or notCount == len(objects):
            return True
        else:
            return False
    else:
        return True
    
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

