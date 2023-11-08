# Задача №49.
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.


# 1. Программа должна выводить данные

# 2. Программа должна сохранять данные в
# текстовом файле

# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)

# 4. Использование функций. Ваша программа
# не должна быть линейной


with open('Phonebook.txt', 'a', encoding = 'utf-8') as phone:
    phone.write('Иван Александрович Попов +79125698741\n')
    phone.write('Виктор Данииловичь Кожимякин +79123214599\n')
    phone.write('Густав Измаилович Дыдыщ +79125649213\n')

def addCont(inpData):                                                                    # добавление контакта
    with open('Phonebook.txt', 'a', encoding = 'utf-8') as cont:
        cont.write(inpData)
        cont.write('\n')

def printAllBook(num):                                                                  # вывод всех контактов
    with open('Phonebook.txt', 'r', encoding = 'utf-8') as allBook:
        for line in allBook:
            print(line.strip())

def nameSearch(searchData):                                                                # поиск по имени\фамилии\номеру телефона
    with open('Phonebook.txt', 'r', encoding = 'utf-8') as name:
            count = 0
            for line in name:
                tempLine = line.split()
                for el in tempLine:
                    if el.lower() == searchData.lower():
                        count += 1
                        print(line.strip())
            if count == 0:
                print('Совпадения не найдены')

mainCount = 1

while mainCount != 0:
    startPage = int(input('-------- Выберите команду --------:\n'                                       # выбор команды
                          '_1) -- Добавить контакт\n'
                          '_2) -- Найти контакт по имени\фамилии\номеру телефона\n'
                          '_3) -- Показать все контакты\n'
                          ':'))
    if startPage == 1:
        inpCont = input('\nВведите все данные контакта в формате " Имя Отчество Фамилия +79012345678 "\n:')
        addCont(inpCont)
    elif startPage == 2:
        inpSearch = input('\nВведите имеющиеся у вас данные контакта(имя / фамилия/ номер телефона "+79......")\n:')
        print('')
        nameSearch(inpSearch)
    elif startPage == 3:
        print('')
        printAllBook(3)

    maybe = int(input('\n----- Желаете совершить дополнительные операции? -----\n'
                      '_1) -- Да\n'
                      '_2) -- Нет\n'
                      ':'))
    if maybe == 1:
        print('')
        mainCount = 1
    else:
        print('\n----------- Спасибо, Досвидания! -----------')
        mainCount = 0


    




                         
