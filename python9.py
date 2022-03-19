#9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
Quater = int(input ('укажите номер четверти системы координат'))
if Quater == 1:
    print('x > 0 and y > 0')
elif Quater == 2:
    print('x > 0 and y < 0')
elif Quater == 3:
    print('x < 0 and y < 0')
elif Quater == 4:
    print('x < 0 and y > 0') 
else:
    print ('данной четверти не существует')