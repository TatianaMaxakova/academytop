mylist = [3, 5, 6, 8, 9, 14, 16, 18, 23, 28, 45, 66, 79]
#посчитать длину
#разделить пополам
#цикл - вывести

#циклом for перебираем все элементы по номерам (через range)
#если элемент есть в списке

def priam_perebor(mylist, elem):
	"""Находит число в списке,
       Возвращает индекс элемента, 
       если его нет - выводит None.
    """
    for i in range(len(mylist)):
		if mylist[i] == elem:
			return i
    # return None


print(priam_perebor(mylist, 9))
print(priam_perebor(mylist, 7))
