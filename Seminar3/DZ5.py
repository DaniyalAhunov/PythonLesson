# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fibonacciPozitiv(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
def fibonacciNegative(n):
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a, b = b, a - b

def fibonacciEnd(n):
    fEnd = list(fibonacciPozitiv(k))
    minusF = list(fibonacciNegative(k))
    for i in range(len(minusF)):
        fEnd.insert(0, minusF[i])
    return fEnd

k = int(input('Введите число k = '))
fibonacci = list(fibonacciEnd(k))
print(fibonacci)
