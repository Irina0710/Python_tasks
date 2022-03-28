#Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

List = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
str_to_find = "qwe"
count = 0
if List.count(str_to_find) < 2:
    print('-1')
countString = 0
countPos = 0
for i in List:
    if str_to_find in i:
        countString += 1
    if countString == 2:
        print(countPos)
    countPos += 1

