Colors = ['red', 'green', 'blue'] #набор данных список
data = open('file.txt', 'a') # связываем текстовую переменную с путем к файлу и указываем тип работы с ним
#a – открытие для добавления данных 
# r – открытие для чтения данных
# w – открытие для записи данных, переписывает а не добавляет
# w+, r+ - смешанные режимы

data.writelines(Colors) #записываем набор данных
data.write('\nline 1\n') #добавляем новую порцию данных, где /n разделитель.Если поставить его перед line тоже, будет добавлятьсч пустьая срока
data.write('line 2\n')
data.close() #закрываем документ

# или другая форма записи, в таком случае закрытие файла автоматически происходит
with open('file.txt', 'w') as data: #принимаем это файл как переменную data
 data.write('line 1\n')
 data.write('line 2\n')

#Чтение:
path = 'file.txt'
data = open(path, 'r')
for line in data:
 print(line)
data.close()
# если в документе хранятся числа, то перед 
# работой с ними нужно их законвертировать из теста в int

