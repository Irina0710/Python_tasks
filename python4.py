#Показать первую цифру дробной части числа
print ('Введите число')
a = float(input())
result = int((a * 10) % 10)
print(result)