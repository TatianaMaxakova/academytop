#Домашнее задание: 
#Пишем себе словарь для слов (не обзательно русско-английских) 
#Изначально словарь пустой. 
#Можно ввести несколько слов. 
#Потом словарь выбирает одно слово и спрашивает, как оно переводится. 
slovar = { 
} 
print  ('Словарь пустой ') 
 
for good in slovar: 
    print('словарь', good, slovar[good]) 
new_good = input('какое слово добавить? ') 
while new_good != 'никакое': 
    new_translate = input('как переводится? ' ) 
    print('перевод добавлен ', new_translate) 
    slovar[new_good] = new_translate 
    new_good = input('Какое слово добавить ещё? ' )  
     
for g in slovar: 
    print(g, slovar[g]) 
from random import choice 
print('Как переводится слово ', 
      choice(list(slovar.keys())))