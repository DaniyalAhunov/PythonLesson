# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lists = []
listEnd = []
endCount = -1

numberInput = input('Введите цифры через пробел: ')
for i in range(0, len(numberInput.split(' '))):
    a = int(numberInput.split(' ')[i])
    lists.append(a)
print(f'Ваш изначальный список: {lists}')

for i in range(len(lists)//2):
    n = lists[i]*lists[endCount]
    listEnd.append(n)
    endCount -= 1

if len(lists)%2 != 0:
    print(f'Произведение пар из списка выше: {listEnd}')
    print(f'число у которого нет пары для перемножения: {lists[len(lists)//2]}')
    
else:
    print(listEnd)