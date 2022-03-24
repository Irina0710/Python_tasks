import hello # вызываем функцию из другого файла, где hello имя файла
print(hello.f(1)) #обратились к функии f из фвйла hello с аргумеетом 1


#Значения по умолчанию для функций
def new_string(symbol, count):
return symbol * count
print(new_string('!', 5)) # ответ !!!!!
print(new_string('!')) # error

# но мы можем
def new_string(symbol, count = 3): #задать сразу
return symbol * count
print(new_string('!', 5)) # ответ !!!!!
print(new_string('!')) # !!! т к по умолчанию 3
print(new_string('4')) # 12

# задаем неограничеснное колво аргументов с помощью *
def concatenatio(*params):
 res: str = ""
 for item in params:
 res += item
 return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError

#Рекурсии
def fib(n):
 if n in [1, 2]:
 return 1
 else:
 return fib(n-1) + fib(n-2)
list = []
for e in range(1, 10):
 list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

# Кортежи (неизменяемые списки) обязательна запятая даже если 1 аргумент 1,
a = (3,4) # пара
print (a) #обращаемся к паре
print (a[0]) # обращаемся к 1му элементу и тд
print (a[-1])# обращаемся к последнему элементу как и в списках и тд

# кортеж в цикле
a = (3,4,5)
for item in a:
    print(item)

# действия с кортежами
t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')


t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
 print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not support
item assignment

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

# Словари
# Неупорядоченные коллекции произвольных
# объектов с доступом по ключу вместо индекса
# типы ключей могут отличаться

dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
 # ключ слева - left и тд. СЛеш стобы не в строку все выводить а в столбик
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
print(dictionary['up']) # ↑

for k in dictionary.keys():
    print(k)
    #печатаем все ключи

for k in dictionary.values():
    print(k)
    #печатаем все значения

dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

# Множества set
# Неупорядоченная совокупность элементов
a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}
a = {1, 2, 3, 5, 8}
b = frozenset(a) #frozenset неизменяемое множество
print(b) # frozenset({1, 2, 3, 5, 8})

#Списки
list = [1,2,3,4,5]
list2 = list 1
for e in list1:
    print(e)     
print()
for e in list2:
    print(e)   
    
     #сделали копию list1
# можем поменять значение элемента в 1 или 2 списке и поменяется во втором соответсвенно
List1[0] = 123
list2[1] = 234

print(list1.pop()) # удаляем последний элемент списка 
print(list1.pop(2)) # удаляем  элемент списка  c индексом 2
print(list1.insert(2, 11)) #вставляем 11 после элемента  c индексом 2
print(list1.append(11)) # вставляем 11 в конец



