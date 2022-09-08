# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
import random
from math import factorial
get_number = input ('Task#1 сумма цифр в числе\nВведите вещественное число: ')
if '-' in get_number:
    get_number = get_number[1:]
if '.' in get_number:
    fl = len(get_number[get_number.index('.')+1:])
    number = int(float(get_number )* 10**fl)
else:
    number = int(get_number)

rez = 0
while number > 0 :
    rez = rez + number %10
    number = number // 10
print('Sum = ', rez)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print('')
get_number2 = int(input ('Task#2 Факториал ряда чисел до N\nВведите целое число: '))
list2 = []
for i in range(1,get_number2+1):
    list2.append(factorial(i))
print(list2)

# # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# не понял условие

# (ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
print('')
N = int(input('Task#3 Произведение указанных в файле чисел\nВведите число диапазона: '))
list1 = []
for i in range(-N , N):
    list1.append(random.randint(0,20))
print('Сгенерированный массив:' , list1)

list_key = []
path = 'data.txt'
file_data = open(path, 'r')
for line in file_data:
    list_key.append(int(line))
print('позиции элементов из файла: ', list_key)


rez = 1
for i in range(len(list_key)):
    rez *= list1[list_key[i]]
print('Произведение элементов = ', rez)

# Реализуйте алгоритм перемешивания списка.

list3 = [1,2,3,4,5,6,7,8,9,10,11]
print('')
print('Task#4 Перемешивание массива\nOriginal list = ', list3)
temp = 0
for i in range(len(list3)):
    rand_index = random.randint(0,len(list3)-1)
    temp = list3[i]
    list3[i] = list3[rand_index]
    list3[rand_index] = temp
print('Shuffled list = ',list3)
    

