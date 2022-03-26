#Определить, присутствует ли в заданном списке строк, некоторое число 
n = int(input('Ввведите  число:  '))
List = ['hello', '123', 'world', '34kdh']
for n in List:
    if n.isdigit():
        print(n)



