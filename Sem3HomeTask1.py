# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

x = [1, 2, 3, 4, 5, 6, 7]
summ = 0
for i in range(1, len(x), 2):
    summ += x[i]       
print(f"{x} -> сумма элементов на нечётных позициях: {summ}")