# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа 
# X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#     Примеры/Тесты:
#     4 4 -> 2 2
#     5 6 -> 2 3
# **Примечание.**
# Вариант 1. Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение - посмотрите  в сети. 
# Обойдите дополнительной проверкой возможность комплексных решений. 
# Можно игнорировать то, что получаться рациональные решения вместо натуральных.
# Для вычисления квадратного корня используйте возведение в степень 0.5 или  
# ```(*)``` **Усложнение.** найдите самостоятельно в сети какая функция стандартной 
# библиотеки вычисляет квадратный корень и как до нее добраться.
# Вариант 2. Решить эту задача можно  "перебором значений" в цикле
import math
productionP=float(input("Введите произведение чисел:"))
sumS=float(input("Введите сумму чисел:"))
print("Вариант 1 решения через дискриминант")
flag=True
if productionP>1000:
    print(f"Введено слишком большое число произведения {productionP}, >1000")
    flag=False
if flag:
    dst=(sumS*sumS)-(4*(-1)*productionP*(-1))
    if dst>= 0:
        number1=((-1)*sumS+(dst**0.5))/(-2)
        number2=((-1)*sumS-(math.sqrt(dst)))/(-2)
        print(f"{number1} {number2}")
    else:
        print(f"Число с произведением {productionP}  и суммой {sumS} является комплексным")
print("Вариант 2 решения табуляцией функции с точностью до 0.1")
i=-10000
number1=-1000000
while i<10000:
    if abs((productionP*sumS)-(productionP+sumS))<0.1:
        number1=i
        number2=productionP/i
        print(f"{number1} {number2}")
        break
    i+=0.001
if number1==(-1000000):
    print(f"Решения не найдено")