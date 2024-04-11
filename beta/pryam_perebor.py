mylist = [3, 5, 6, 8, 9, 14, 16, 18, 23, 28, 45, 66, 79]
#Находит число в списке,
#Возвращает индекс элемента, 
#если его нет - выводит None.
  
def priam_perebor(mylist, elem):
    for i in range(len(mylist)):
	    if mylist[i] == elem:
	        return i
#return None


print(priam_perebor(mylist, 9))
print(priam_perebor(mylist, 7))
