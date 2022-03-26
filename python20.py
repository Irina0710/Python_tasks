#Определить, присутствует ли в заданном списке строк, некоторое число 
List = ['hello', '22', 'world', '34kdh']
for i in List:
    if i.isdigit():
        print(i)

n = int(input('Ввведите  число:  '))

if i == n:
    print(f'Число {n} присутвтует в списке')
else:
    print(f'Число {n} отсутвует в списке')
