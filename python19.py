#Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
from random import shuffle
import time 
def accident(start, stop):
    sequence = [items for items in range(start, stop + 1)]
    seconds = str(time.time())
    index = int(seconds[len(seconds) - (len(str(stop)) - 1):])
    shuffle(sequence)
    return sequence[index]

print(accident(1,10))