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

result = []

for key, value in group.items():
    for key1, value1 in value.items():
        result.append((key, key1, value1))

print(result)