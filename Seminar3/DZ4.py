# Напишите программу, которая будет преобразовывать десятичное 
# число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Число которое хотите перевести: '))
dobleNum = ''
while number > 0:
    dobleNum = str(number % 2) + dobleNum
    number = number // 2
print(f'Двоичная: {dobleNum}')