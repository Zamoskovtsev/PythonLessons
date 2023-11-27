
def fraction_check(num):
    result = num
    print(num % 50)
    if num % 50 != 0:
        logger.error(f"Ввод числа не кратного 50 {num}")
        result = 0
        logger.info(f"Параметр {num}  не кратен 50, введенное число заменено на 0")
    return result

def gross_log_check(str_oper:str,change:float,grossmoney:float):
    logger.info(f"{str_oper} {change} Остаток на счете: {grossmoney}")
    return

def get_summ_money(operation:str) -> float:
    money=float(input(f'Введите сумму {operation} кратно 50: '))
    print(money)
    money=fraction_check(money)
    return money

def replenishment(money: float,count_r:int,gross_m:float) -> float:
    gross_m=gross_m+money
    if count_r==3:
        gross_m=gross_m*1.03
        gross_log_check("начислено %",gross_m*0.03, gross_m)
    return gross_m
    
def withdrawal(money: float,gross_m:float) -> float:
    percent=money*0.015
    if percent<30:
        percent=30
    if percent>600:
        percent=600
    if gross_m<(money+percent):
        print(f'Снятие суммы {money} невозможно, недостаточно средств')
    else:
        gross_m=gross_m-money-percent
        gross_log_check("% за снятие",percent, gross_m)
    return gross_m

def luxury(gross_m:float) ->float:
    if gross_m>=5000000:
        gross_m=gross_m*0.9
        gross_log_check("% за роскошь",gross_m*0.1, gross_m)
    return gross_m

def list_operations(fin_oper:str,balance:float)-> list:
    return [fin_oper,balance]
  

import os
import logging
logging.basicConfig(level=logging.INFO, filename="chech_gross.log", encoding="utf-8")
logger = logging.getLogger(__name__)


gross_money = 0
count_r=0
choise=0
operations=[['Начальный остаток',gross_money]]

while choise!=1:
    print('Введите 1 для выхода из банкомата')
    print('Введите 2 пополнения')
    print("Введите 3 снятия")
    choise = int(input('Ваш выбор: '))
    if choise == 1:
        print('Вы выбрали выход')
        for item in operations:
            print(item)
        False
    if choise == 2:
        if count_r<=3:
            count_r+=1
        else:
            count_r=0
        print("выбрано пополнение")
        gross_money=replenishment(get_summ_money('пополнения'),count_r,gross_money)
        gm=gross_money
        operations.append(list_operations('Пополнение',gross_money))
        gross_money=luxury(gross_money)
        if gm != gross_money:
            operations.append(list_operations('Снят налог на роскошь',gross_money))
        print(f'Сумма на счете {gross_money}')     
    if choise == 3:
        print("выбрано снятие")
        gross_money=withdrawal(get_summ_money('снятия'),gross_money) 
        operations.append(list_operations('Снятие',gross_money))
        gm=gross_money
        gross_money=luxury(gross_money)
        if gm != gross_money:
            operations.append(list_operations('Снят налог на роскошь',gross_money))
        print(f'Сумма на счете {gross_money}')
