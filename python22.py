#Найти сумму чисел списка стоящих на нечетной позиции
List_1 = [1,4,5,6,4,6,3,5,2,4]
summary = 0
for i in range(1,len(List_1),2): #делаем шаг2. Еще можем посмтореть остаток от деления на 2 каждого индекса
    summary+=List_1[i]
print(summary)
