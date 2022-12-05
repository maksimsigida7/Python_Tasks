# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

from random import randint

number = int(input('Введите размер списка '))
list_first = []
list_second = []

for i in range(number):
    list_first.append(randint(0, 9))

for i in range(len(list_first)):
    while i < len(list_first)/2 and number > len(list_first)/2:
        number = number - 1
        a = list_first[i] * list_first[number]
        list_second.append(a)
        i += 1

print(list_first)
print(list_second)