# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

def maxNum(list):
        max = list[0]-int(list[0])
        for i in range(len(list)):
                x = list[i] - int(list[i])
                if x > max:
                        max = x
        return max
def minNum(list):
        min = list[0]-int(list[0])
        for i in range(len(list)):
                x = list[i] - int(list[i])
                if x < min:
                        min = x
        return min

list = [1.1, 1.2, 3.1, 10.01]
maxNum = round(maxNum(list),2)
minNum = round(minNum(list),2)
print(f'''Максимальная дробная чатсть {maxNum}
Минимальная дробная чатсть {minNum}
Разнича между ними {maxNum - minNum}''')