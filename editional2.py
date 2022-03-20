# при заданном целом числе n посчитайте n + nn + nnn
from tkinter import N


n = (input('введите число'))
nn = n + n 
nnn = n + n + n 
sum = int(n) + int(nn) + int(nnn)
print(sum)
