#4) Пользователь вводит  строку и символ. Необходимо определить индексы
# первого и последнего вхождения символа в строке.


print ('Введите строку')
string1 = input()
print ('Введите символ')
symbol = input()

first_match_index = string1.find (str(symbol))
last_match_index = string1.rfind (str(symbol))

print('Farst symbol index:' + str (first_match_index))
print('Last symbol index:' + str (last_match_index))