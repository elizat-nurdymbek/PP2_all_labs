x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#output
#Orange
#Banana
#Cherry

#Примечание: Убедитесь, что количество переменных соответствует количеству значений, иначе возникнет ошибка.

#Одно значение для нескольких переменных  
#Вы также можете присвоить одно и то же значение нескольким переменным в одной строке:
    
x = y = z = "Orange"

print(x)
print(y)
print(z)

#output
#Orange
#Orange
#Orange

#Распаковка коллекции  
#Если у вас есть коллекция значений в виде списка, кортежа и т. д., Python позволяет извлекать значения в переменные. Это называется распаковкой.
 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#output
#apple
#banana
#cherry