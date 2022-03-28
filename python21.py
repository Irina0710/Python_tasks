#Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
from ast import Index
from re import X


List = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
str_to_find = "qwe"
count = 0
if List.count(str_to_find) < 2:
    count = -1 #сделали проверку есть ли второе вхождение
else:
    for i in range(len(List)): #считаем индексы
        if List[i] == str_to_find:
            count+=1
            if count == 2:
                count = i
                break

print(f'Искомое {str_to_find}, ответ {count}')

# или номер номер первого вхождения можно найти через X

# x = List.find(str_to_find)
# print(x) 
# или через Index
# for i in List:
#     if i == str_to_find:
#         print(i)

# index = List.index(str_to_find)
# print(index)
        
        
