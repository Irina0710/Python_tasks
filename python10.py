# Найти расстояние между двумя точками пространства
#A B = √ (x B − x A) 2 + (y B − y A) 2 (формула нахождения)
x1 = int(input('Введите координаты x первой точки '))
y1 = int(input('Введите координаты y первой точки '))
x2 = int(input('Введите координаты x второй точки '))
y2 = int(input('Введите координаты y второй точки '))
S = ((x2 - x1)**2 + (y2 - y1)**2)**(0.5)
print(f'расстояние между точками: {S}')
