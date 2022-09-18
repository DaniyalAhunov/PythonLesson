# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from pathlib import Path


def encode(s):
 
    encoding = "" # сохраняет выходную строку
 
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding
def file_reading(x: str):
    with open(x, 'r') as f:
        y = f.readline()
    return y
def file_saving(sFile: str, x: str):
    with open(sFile, 'a') as f:
        f.write(f'{x}\n')


file_open = 'PythonGB/File/s5dz4.txt' 
file_save = 'PythonGB/File/s5dz4(exit).txt'
s = file_reading(file_open)
print(f'Входная строка: {s}')
kod_mini = encode(s)
file_saving(file_save, kod_mini)
print(f'Закодированая строка {kod_mini}')
 