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


def deleteCont(surname):
    phone_book = read_txt('phonebook.txt')
    with open('Phonebook.txt', 'w+', encoding = 'utf-8') as phonebook:
        count = 0
        for line in phonebook:
            count += 1
            tempLine = line.split()
            for el in tempLine:
                if el.lower() == surname.lower():
                    phone_book.pop(count - 1)
                    print(phone_book)
            phonebook.write(phone_book)



def read_txt(filename):
    phone_book = []
    with open(filename, 'r', encoding = 'utf-8') as phb:
        for line in phb:
            phone_book.append(line)
    return phone_book



mainCount = 1

while mainCount != 0:
    startPage = int(input('-------- Выберите команду --------:\n'                                       # выбор команды
                          '_1) -- Добавить контакт\n'
                          '_2) -- Найти контакт по имени\фамилии\номеру телефона\n'
                          '_3) -- Показать все контакты\n'
                          '_4) -- Изменить контакт\n'
                          '_5) -- Удалить контакт\n'
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
    elif startPage == 5:
        inpSurname = input('\nВведите фамилию контакта, который желаете удалить')
        print('')
        deleteCont(inpSurname)

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


    
#-----------------------------------------------------------------

# def show_menu():
#     print('1. Распечатать справочник\n'
#           '2. Найти телефон по фамилии\n'
#           '3. Изменить номер теоефона\n'
#           '4. Удалить запись\n'
#           '5. Найти абонента по номеру телефона\n'
#           '6. Дабавить абонента в справочник\n'
#           '7. Закончить работу\n')
#     choice = int(input())
#     return choice

# def work_with_phonebook():
#     choice = show_menu()
#     phone_book = read_txt('phonebook.txt')
#     while (choice != 7):
#         if choice == 1:
#             print_result(phone_book)
#         elif choice == 2:
#             last_name = input('lastname')
#             print(find_by_lastname(phone_book, last_name))
#         elif choice == 3:
#             last_name = input('lastname')
#             new_number = inpit('new number')
#             print(change_number(phone_book, last_name, new_number))
#         elif choice == 4:
#             lastname = input('lastname')
#             print(delete_by_lastname(phone_book, lastname))
#         elif choice == 5:
#             number = input('number')
#             print(find_by_number(phone_book, number))
#         elif choice == 6:
#             user_data = input('new data')
#             add_user(phone_book, user_data)
#             write_txt('phonebook.txt', phone_book)

#         choice = show_menu()


# def read_txt(filename):
#     phone_book = []
#     fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
#     with open(filename, 'r', encoding = 'utf-8') as phb:
#         for line in phb:
#             record = dict(zip(fields, line.split(',')))
#             phone_book.append(record)
#     return phone_book

# def write_txt(filename, phonebook):
#     with open(filename, 'w', encoding = 'utf-8') as phout:
#         for i in range(len(phonebook)):
#             s = ''
#             for v in phonebook[i].valuse():
#                 s += v + ','
#             phout.write(f"{s[:-1]}\n")


# work_with_phonebook()



                         
