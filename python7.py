#Проверить истинность утверждения ¬(X ⋁ Y  ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def is_true(x,)

X = False
Y = True
Z = False
print(f'Исходные данные: X = {X}, Y = {Y}, Z = {Z}')

for X in range(0, 2):
    for Y in range(0, 2):
        for Z in range(0, 2):
            r1 = not (X or Y or Z)
            r2 = not (X) and not (Y) and not (Z)

if r1 == r2:
    print('True ')
else:
    print ('False')
