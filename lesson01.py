# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
from ast import While
from math import sqrt
from operator import truediv
from webbrowser import Elinks


a = int(input ('Введите день недели цифрой 1-7 ...'))
if a > 7 or a < 1: print('Нет такого дня')
if a == 6 or a ==7:
    print('Это выходной!')
else:
    print('всем работать')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
X = True
Y = True
Z = True

for i in range(2):
    for j in range(2):
        for k in range(2):
            print ("X = {}, Y = {}, Z = {}".format(X , Y, Z))
            if not (X or Y or Z) == (not X and not Y and not Z):
                print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z   => True')
            else:
                print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z   => False')
            Z = not Z
        Y = not Y
    X = not X

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
coord = [int(i) for i in input("Введите координаты X, Y...").split(',')]
if coord[0] > 0 and coord[1] > 0:
    print(coord, '-> первая четверть')
elif coord[0] < 0 and coord[1] > 0:
    print(coord, '-> вторая четверть')
elif coord[0] < 0 and coord[1] < 0:
    print(coord, '-> третья четверть')
elif coord[0] > 0 and coord[1] < 0:
    print(coord, '-> четвертая четверть')
elif coord[0] == 0:
    print(coord, 'точка лежит на оси Х')
elif coord[0] == 0:
    print(coord, 'точка лежит на оси Y')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

coord_first= [int(i) for i in input("Введите координаты первой точки X, Y...").split(',')]
coord_second = [int(i) for i in input("Введите координаты второй точки X, Y...").split(',')]
dist_x = coord_second[0] - coord_first[0]
dist_y = coord_second[1] - coord_first[1]
dist = round( sqrt(pow(dist_x,2)+pow(dist_y,2)), 4)
print('Расстояние между точками = ', dist)