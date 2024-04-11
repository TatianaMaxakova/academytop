#Создать словарь: студент и СЛОВАРЬ его оценок (дата - оценка)
#С помощью форматирования строк вывести табличку:
from datetime import datetime
group = {
    'Вася': {
        datetime(2024,3,10):8,
        datetime(2024,3,12):6,
    },
    'Ася': {
        datetime(2024,3,10):10,
        datetime(2024,3,12):12,
    },
    'Мася': {
        datetime(2024,3,10):8,
        datetime(2024,3,12):10,
    },
} 
#valuelist = [group [key] for key in group]
#print(valuelist)
#for k in group:
 #   print(k, group[k])
  #  
#student1 = group.get('Вася', datetime(2024,3,10))
#student2 = group.get('Ася', datetime(2024,3,10))
#student3 = group.get('Мася', datetime(2024,3,10))
#print(student1, student2, student3)

for k in group:
    print(k, group[k]) 
#print(group['Вася'])  
#print(group['Ася'])
#print(group['Мася'])
    







