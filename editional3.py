#сложите цифры целого числа
n = int(input('введите целое число: '))
sum = 0
while n:
    sum += n % 10
    n = n // 10
print(sum)