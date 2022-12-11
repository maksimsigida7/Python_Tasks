# В файле находится Н натуральных числа, записаных через пробел.
# Среди чисел не хватает одного, чтобы выполнить условия A[i] - 1 = A[i-1].
# Найдите это число.
# Пример: 1 2 3 4 6 7
# Вывод: 4


path = 'E:\Programs\Get\Python_Seminars\Sem5Task1File.txt' # Задали путь к файлу
data = open(path, 'r') # Открыли файл
string = data.read()   # Прочитали файл
data.close()           # Закрыли файл

list = [int(i) for i in string.split()]
print(list)
for i in range(len(list) - 1):
	if list[i + 1] != list[i] + 1:
		print (list[i] + 1)