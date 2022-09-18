# 1. Вычислить число c заданной точностью *d*
#     *Пример:* 
#     - при $d = 0.001, π = 3.141

from math import factorial as fact
def pii():
    i = 1
    sgn = -1
    a = 13591409
    b = 545140134
    c = 640320
    d = c ** (3/2)
    s = a / d 
    ss = 3
    while str(ss)[:12] != '3.1415926535' :
        tmp = (sgn * fact(6*i) * (a + b*i) / 
        (fact(3*i) * fact(i) ** 3 * d * c**(3*i)))
        s += tmp
        sgn *= -1
        i += 1
        ss = 1 / (12*s)
    return ss

d = int(input('Введите число c заданной точностью(сколько необходимо знаков после запятой): '))
ss = pii()
ss1, ss2 = str(ss).split('.')
print(float(f'{ss1}.{ss2[:d]}'))