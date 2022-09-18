# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# # Вариант 1
# def maxNum(list):
#         max = list[0]
#         for i in range(len(list)):
#                 x = list[i]
#                 if x > max:
#                         max = x
#         return max
# def minNum(list):
#         min = list[0]
#         for i in range(len(list)):
#                 x = list[i]
#                 if x < min:
#                         min = x
#         return min
# lists = []
# numberInput = input('Введите цифры через пробел: ')
# for i in range(0, len(numberInput.split(' '))):
#     a = int(numberInput.split(' ')[i])
#     lists.append(a)
# print(f'максимально число из вашего списка: {maxNum(lists)}')
# print(f'максимально число из вашего списка: {minNum(lists)}')

# # Вариант 2
# def mim_and_max(lst):

#     print(lst)
#     print(max(lst), min(lst))

# lst = input('Enter number: ')
# lst = lst.split(' ')
# lst = list(map(int, lst))
# print(lst)
# mim_and_max(lst)


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     1) с помощью математических формул нахождения корней квадратного уравнения

# a = int(input('Введите число А: '))
# b = int(input('Введите число B: '))
# c = int(input('Введите число C: '))
# d = b ** 2 - 4 * a * c
# if d < 0:
#     print('Нет корней')
# elif d == 0:
#     x = (-d) / 2 * a
#     print(x)
# else:
#     x_1 = ((-b) + d ** (1 / 2)) / 2 * a
#     x_2 = ((-b) - d ** (1 / 2)) / 2 * a
#     print(x_1, x_2)

#     *2) с помощью дополнительных библиотек Python

# from sympy.solvers import solve
# from sympy import Symbol


# def fun(a, b, c):
#     x = Symbol('x')
#     return solve(f'{a}*x**2+{b}*x+{c}', x)

# a = int(input('Введите число А: '))
# b = int(input('Введите число B: '))
# c = int(input('Введите число C: '))
# print('Корни уравнения:', *fun(a, b, c))

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.

import math
num_1 = int(input('Введите число: '))
num_2 = int(input('Введите второе число: '))
print(math.lcm(num_1, num_2))
with open('file.txt', 'w') as f:
    f.write(str(math.lcm(num_1, num_2)))