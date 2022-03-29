# Написать программу преобразования десятичного числа в двоичное
print('введите число')
number = 31
binary_number = []
while number >=1:
    binary_digit = number%2
    number = number // 2
    binary_number.append(binary_digit)
print(binary_number)