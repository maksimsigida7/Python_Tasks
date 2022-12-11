# Задача2.
# Напишите программу, удаляющую из текста все слова, содержащие
# "абв". Строка находится в файле.
# Пример: лоало лалоар ыгшва сиирв ырашгр врпрвабв апров
# Вывод: лоало лалоар ыгшва сиирв ырашгр апров

path = 'E:\Programs\Get\Python_Seminars\Sem5Task2File.txt'
data = open(path, 'r', encoding='UTF-8')
string = data.read()
data.close()

list0 = string.split()
print(list0)
list1 = list(filter(lambda x: not 'абв' in x, list0))
print(list1)