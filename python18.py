#Реализовать алгоритм перемешивания списка. 
import random

List = [2, 124, 345, 245, 245, 4, 3, 1]
print(List)
listLenght = len(List)
for i in range(0, listLenght):
    somedigit = random.randrange(0, listLenght)
    List[i], List[somedigit] =  List[somedigit],  List[i]
print(List)

