# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

import math

Ax = int(input('Введите координату X точки A '))
Ay = int(input('Введите координату Y точки A '))
Bx = int(input('Введите координату X точки B '))
By = int(input('Введите координату Y точки B '))

AB = math.sqrt(((Bx - Ax)**2) + ((By - Ay)**2))

#Сокращение знаков до 2х после запятой без округлений
def Reduction(AB):
    if type(AB) == float:
        AB = str(AB).split('.')
        if len(AB[1]) > 1:
            AB = AB[0] + "." + AB[1][0] +  AB[1][1]
        else:
            AB = AB[0] + "." + AB[1][0]
        return float(AB)
    else:
        return AB

print(f'A ({Ax},{Ay}); B ({Bx},{By}) -> {Reduction(AB)}')
