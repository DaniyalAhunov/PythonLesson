# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
from collections import Counter

def listOff(korteg, listNum):
    for i in range(len(korteg)):
        endNum = korteg[i][0]
        listNum.insert(0,endNum)
    return listNum

start = [10, 10, 23, 10, 123, 66, 78, 123]
# start = [1, 1, 2, 3, 4, 5, 5] -- перепроверка
korteg = Counter(start).most_common()[:1:-1]
endList = []
print(listOff(korteg, endList))

    