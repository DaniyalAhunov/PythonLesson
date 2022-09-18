# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     *Пример:* 
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
from pathlib import Path

def FunctionM (k: int):
    end_fun = ''
    while k >= 0:
        kef = random.randint(0, 101)
        if k == 1:
            end_fun += f'{kef}*x +'
        elif k == 0:
            end_fun += f' {kef} = 0'
        else:
            end_fun += f'{kef}*x^{k} + '
        k = k - 1
    return end_fun

file_1 = 's3dz4.txt'
# file_2 ='s3dz4(1).txt' # -- что бы создать второй файл(для следующего домашнего задания)
home = Path.home()
wave = Path(home,'FileSeminar', file_1)

k = int(input('Введите число k: '))
strr = FunctionM(k)
print(f'Многочлен: {strr}')
with open(wave, 'a') as f:
    f.write(f'{strr}\n')
