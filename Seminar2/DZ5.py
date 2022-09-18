# Реализуйте алгоритм перемешивания списка.
import random


srtStart = input('Введите свою строку (пока что только через пробел) : ')
srtSplit = srtStart.split(' ')
random.shuffle(srtSplit)
srtEnd = ' '.join(srtSplit)
print(f'Перемешаная введеная вами строка: {srtEnd}')