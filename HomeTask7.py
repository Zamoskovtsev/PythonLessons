# Напишите функцию группового переименования файлов. Она должна:
    #принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    # принимать параметр количество цифр в порядковом номере.
    # принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
    # принимать параметр расширение конечного файла.
    # принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] 
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, 
# если оно передано. Далее счётчик файлов и расширение. 
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from string import ascii_lowercase, digits
from random import randint, choices
import pathlib
import os
        
def rename_file(file_path:str,
    file_mask:str,
    number:int,
    ext1:str,
    ext2:str,
    startname:int,
    stopname:int
    ):
    number=4
    os.chdir(file_path)
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    numfile=0
    for file in file_name:
        name,ext=file.split('.')
        if ext==ext1:
            os.rename(file,f'{name[startname:stopname]}{file_mask}{numfile:0{number}}.{ext2}')
            numfile+=1
       
def HBZ(ext:str='txt', 
        min_name:int=6, 
        max_name:int=30, 
        min_size:int=256, 
        max_size:int=4096, 
        count_files:int=10
        ):
        for i in range(count_files):
            name_file=(''.join(choices(ascii_lowercase+digits, k = randint(min_name,max_name)))) #Данные в файл
            date_file_body=bytes(randint(0,255) for i in range(randint(min_size,max_size))) # имя файла
            if os.path.exists(f'{name_file}.{ext}'): #проверка на существование файла в текущес каталоге
                continue #перейти к следующей итерации
            with open(f'{name_file}.{ext}','wb') as date: # открыть файл
                date.write(date_file_body) # запись в файл данных
                
def HBZ2(direct, **kwargs):
    if not os.path.exists(direct):
        os.mkdir(direct) #создание директории
    os.chdir(direct) # переключение в директорию
    for ext, count in kwargs.items(): # создание количества файлов с указанными расширениями
        HBZ(ext,count_files=count)         


if __name__ == '__main__':    
    rename_file(r'C:\Users\zamoskal\OneDrive - Danone\Проекты\Обучение Python\Python main\s100','task', 4,'txt','doc',2,4)
