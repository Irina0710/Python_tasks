# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда[ 1, 2, 6, 24 ]
mult = []
n=1
for i in range(4):
    mult.append(n)
    n*=n+1
print(mult)
