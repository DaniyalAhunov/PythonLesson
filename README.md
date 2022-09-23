# **_Python обучение GB_**

[Семинар 1](https://github.com/DaniyalAhunov/PythonLesson/tree/main/Seminar1)
<details><summary>Первый семинар. Решение заданий</summary> 

  1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
  Пример:
  - 6 -> да
  - 7 -> да
  - 1 -> нет
  
  2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Где Х,Y,Z = 0 и 1
  
  3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
  Пример:
  - x=34; y=-30 -> 4
  - x=2; y=4-> 1
  - x=-34; y=-30 -> 3
  
  4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)
  
  5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
  - A (3,6); B (2,1) -> 5,09
  - A (7,-5); B (1,-1) -> 7,21
</details>

[Семинар 2](https://github.com/DaniyalAhunov/PythonLesson/tree/main/Seminar2)  
<details><summary>Второй семинар. Решение заданий</summary>

1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
  - 0,56 -> 11
  
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
  - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
  
3.  Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных пользователем через пробел позициях.

5. Реализуйте алгоритм перемешивания списка.
</details>

[Семинар 3](https://github.com/DaniyalAhunov/PythonLesson/tree/main/Seminar3)
<details><summary>Третий семинар. Решение заданий</summary>

1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
  - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.
Пример:
  - [2, 3, 4, 5, 6] => [12, 15, 16];
  - [2, 3, 5, 6] => [12, 15]
  
  3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
  - [1.1, 1.2, 3.1, 10.01] => 0.19

4. Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
Пример:
  - 45 -> 101101
  - 3 -> 11
  - 2 -> 10

5. Задайте число. Составьте список чисел Фибоначчи,
 в том числе для отрицательных индексов.
Пример:

  - для k = 8 список будет выглядеть так: 
   [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
</details>

[Семинар 4](https://github.com/DaniyalAhunov/PythonLesson/tree/main/Seminar4)
<details><summary> Четвертый семинар. Решение заданий</summary>

1. Вычислить число c заданной точностью *d*
Пример:
  - при $d = 0.001, π = 3.141

2. Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N.
Пример:
  "20" -> [2, 2, 5]

3. Задайте последовательность чисел. Напишите программу, которая выведет список 
неповторяющихся элементов исходной последовательности.
Пример:
  [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример: 
  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

5. Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
</details>

[Семинар 5](https://github.com/DaniyalAhunov/PythonLesson/tree/main/Seminar5)
<details><summary> Пятый семинар. Решение заданий</summary>

1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

2. Создайте программу для игры с конфетами человек против человека.
  Условие задачи: 
  На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
  Все конфеты оппонента достаются сделавшему последний ход. 
  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    a) Добавьте игру против бота
    b) Подумайте как наделить бота ""интеллектом""

3. Создайте программу для игры в ""Крестики-нолики"" с интерфейсом

4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
</details>

[Семинар 6](https://github.com/DaniyalAhunov/PythonLesson/tree/main/Seminar6)
<details><summary> Шестой семинар. Решение заданий</summary>

Задание на все файлы:

  Задача: предложить улучшения кода для уже решённых задач (3-5 задач):
  С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
</details>