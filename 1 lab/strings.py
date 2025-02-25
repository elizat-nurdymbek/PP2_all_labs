#В Python строки могут быть заключены в одинарные или двойные кавычки.

#'hello' — это то же самое, что и "hello".

#Вы можете вывести строковый литерал с помощью функции print():

print("Hello")     #Hello
print('Hello')     #Hello

#Вы можете использовать кавычки внутри строки, при условии, что они не совпадают с кавычками, окружающими строку:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#It's alright
#e is called 'Johnny'
#He is called "Johnny"

a = "Hello"
print(a)

#Hello

#Вы можете присвоить многострочную строку переменной, используя три кавычки:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Примечание: в результате разрывы строк вставляются в том же месте, где они находятся в коде.

#Как и многие другие популярные языки программирования, строки в Python представляют собой массивы байтов, представляющих символы Unicode.

#Однако в Python нет отдельного типа данных для символов, один символ — это просто строка длиной 1.

#Для доступа к элементам строки можно использовать квадратные скобки.

#Получить символ на позиции 1 (помните, что первый символ имеет позицию 0):
a = "Hello, World!"
print(a[1]) #e

#Поскольку строки — это массивы, мы можем пройтись по символам строки с помощью цикла for.

#Пройти по буквам в слове "banana":

for x in "banana":
  print(x)
  
#b
#a
#n
#a
#n
#a

#Функция len() возвращает длину строки:

a = "Hello, World!"
print(len(a)) #13

#Чтобы проверить, присутствует ли определенная фраза или символ в строке, можно использовать ключевое слово in.
txt = "The best things in life are free!"
print("free" in txt) #True



