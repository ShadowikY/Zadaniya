#1) Пользователь вводит строку и символ. Определить количество вхождений символа
# в строку, независимо от регистра, при этом нельзя использовать метод count.


print ('Введите строку')
list_one = input()
print ('Введите символ')
symbol = input()
count = 0

list_one = list_one.lower()

print (list_one)

for i in list_one:
    if i == symbol:
        count = count + 1

print ("Количество вхождений символа: " + str(count))