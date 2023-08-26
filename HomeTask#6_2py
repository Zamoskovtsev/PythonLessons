# 6.2[32]: Определить индексы элементов  массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]
def minmax(lst_1: list, min_lst:int, max_lst:int)-> list:
    lst_2=[]
    for i, element in enumerate(lst_1):
        if min_lst<=element<=max_lst:
          lst_2.append(i)
    return lst_2

def minmax_cortege(lst_1: list, min_lst:int, max_lst:int)-> list:
    lst_2=[]
    for i, element in enumerate(lst_1):
        ctg=(i,element)
        if min_lst<=element<=max_lst:
            lst_2.append(ctg)
    return lst_2

lst=[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minl=2
maxl=10
print(minmax(lst,minl,maxl))
print(minmax_cortege(lst,minl,maxl))
