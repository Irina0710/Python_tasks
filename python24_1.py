# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части 
# элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
float_spisok = [1.1, 1.2, 3.1, 5.002, 10.000001, 11.13, 10.11, 122324.52, 0.14]
# i=0
# while float_spisok[i]>1:
max = 0.000
min = 1.000
for i in range(len(float_spisok)):
    float_spisok[i]=round(float_spisok[i]-int(float_spisok[i]),10) #отняли целую часть и сотавили только дробные
    if max<float_spisok[i]:
        max = float_spisok[i]
    if min>float_spisok[i]:
        min = float_spisok[i]
x=max-min
# print(float_spisok)
# print(max(float_spisok))
print(max,min)
print(type(x))
print(x)