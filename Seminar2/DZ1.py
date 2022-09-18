# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11
sum = 0
number = input('Введите вещественное число: ')
for i in range(len(number)):
    result = number[i].isdigit()
    if result == True:
        sum += int(number[i])
print(sum)