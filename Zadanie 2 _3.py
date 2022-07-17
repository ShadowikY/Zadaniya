# 3) Пользователь вводит строку и символ. Определить количество
# вхождений символа в строку, независимо от регистра.

print ('Введите строку')
string1 = input()
print ('Введите символ')
symbol = input()

symbol = symbol.lower()
string1 = string1.lower()
counter = string1.count(str(symbol))

print ("Количество вхождений символа:"  + str(counter))