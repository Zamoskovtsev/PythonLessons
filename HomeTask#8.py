
def get_user_data() -> list:
    name = input('Введите имя: ')
    sur_name = input('Введите фамилию: ')
    phone_num = input('Введите номер телефона: ')
    desc = input('Введите описание: ')
    return [name,sur_name,phone_num,desc]

def create_record(gb_phone_book: list, user_data: list) -> list:
    gb_phone_book.append(user_data)
    return gb_phone_book


def print_phone_book(gb_phone_book:list) -> None:
    for record in gb_phone_book:
        print(record)

def get_string(message:str) -> str:
    return input(message)

def create_from_data(gb_phone_book: list,file_name:str,delimiter:str ) -> list:
    path_sourse= os.path.join ('.',file_name)
    with open(path_sourse,'r', encoding='utf-8') as sourse:
        for line in sourse:
            gb_phone_book=create_record(gb_phone_book,line.strip().split(delimiter))
    return gb_phone_book

def Write_data_to_file(gb_phone_book: list, file_name: str) ->None:
    path_sourse= os.path.join ('.',file_name)
    with open(path_sourse,'w', encoding='utf-8') as phone_data:
       for record in gb_phone_book:
            phone_data.write(f"{','.join(record)}\n")
            
def find_record_in_FB(gb_phone_book: list, FindStr: str) -> int:
    for idx in range(len(gb_phone_book)):
        if ','.join(gb_phone_book[idx]).startswith(FindStr)==True:
            return idx
    return 1000000000
        
def record_update(gb_phone_book:list, record:list , idx:int) ->list:
    gb_phone_book[idx]=record
    return  gb_phone_book

                               
#def menu():
import os
phone_book = list()
choise=0
while choise!=1:
    print('Введите 1 для выхода из справочника')
    print('Введите 2 для создания новой записи')
    print("Введите 3 для вывода на экран")
    print("Введите 4 для импорта данных из файла")
    print("Введите 5 для сохранения справочника в файл")
    print("Введите 6 для поиска записи в справочнике")
    print("Введите 7 для исправления записи")
    choise = int(input('Ваш выбор: '))
    if choise == 1:
        print('Вы выбрали выход')
        False
    if choise == 2:
        phone_book = create_record(phone_book, get_user_data())
    if choise == 3:
        print_phone_book(phone_book)
    if choise == 4:
        phone_book=create_from_data(phone_book,get_string("Введите имя файла: "),',')
        #get_string("Введите имя файла: "),',')
    if choise == 5:
        Write_data_to_file(phone_book,get_string("Введите имя файла: "))
    if choise == 6:
        record_fnd=find_record_in_FB(phone_book,get_string("Введите начало фамилии: "))
        if record_fnd!=1000000000:
            print(phone_book[record_fnd])
        else:
            print("Запись не найдена")
    if choise == 7:
        record_fnd=find_record_in_FB(phone_book,get_string("Введите начало фамилии для поиска записи для редактирования: "))
        if record_fnd!=1000000000:
            print(phone_book[record_fnd])
            record=get_user_data()
            phone_book=record_update(phone_book, record , record_fnd)
        else:
            print("Запись не найдена")
