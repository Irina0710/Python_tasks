#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.
N=[]
Num = int(input('Введите число '))
n = 1
for i in range(Num):
    N.append(n)
    n*=-3
print(N)