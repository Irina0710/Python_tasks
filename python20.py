#Определить, присутствует ли в заданном списке строк, некоторое число 
string_list = ['hello', '123', 'world', '34kdh']
item_to_find = input ('Введите число')
flag = True
for i in string_list:
    if flag == False:
        break
    elif i == item_to_find:
        print(f"Искомое число {item_to_find} есть в списке")
        flag = False
if flag==True:
    print(f'Искомое число {item_to_find} отсутствует в списке')

