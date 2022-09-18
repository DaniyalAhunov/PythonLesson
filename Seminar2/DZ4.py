# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random
priz = 1
N = int(input('Введите количество элементов: '))
listN = []
for i in range(0, N):
    num = random.randint(N * -1, N)
    listN.append(num)
print(f'Список готов \n{listN}')
pozit = input('Введите место элементов через пробел(нумерация от 0): ') 
for i in range(0, len(pozit.split(' '))):
    a = int(pozit.split(' ')[i])
    priz *= listN[a]
print(f'Произведение выбранных позиций: {priz}')