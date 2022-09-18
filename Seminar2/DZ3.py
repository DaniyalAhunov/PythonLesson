# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
kNum = int(input('Введите число K: '))
list = []
sum = 0
for i in range(1, kNum+1):
    functionK= (1 + 1 / kNum) ** kNum
    # list.append(functionK)
    list.append(round(functionK, 2))
print(f'Список чисел:\n{list}')
for i in range(0, len(list)):
    sum += list[i]
print(f'Сумма всего списка: {sum}')
# print(f'Сумма всего списка: {round(sum, 2)}') -- если нужно два знака после запятой