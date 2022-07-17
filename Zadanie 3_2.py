#2) Пользователь вводит  строку и символ. Необходимо определить индексы первого
#и последнего вхождения символа в строке, при этом нельзя использовать строковые методы для поиска.


print ('Введите строку')
list_one = input()
print ('Введите символ')
symbol = input()
count = 0
index =0
list_temp =[]


list_one = list_one.lower()

print (list_one)

for i in list_one:
    index = index + 1
    if i == symbol:
        count = count+1
        list_temp.append(index)
        print (count)
  #  print ('index' + str(index))
# print (list_temp)
print ("Индекс первого вхождения -", list_temp [0], "\nИндекс последнего вхождения -", list_temp [-1])