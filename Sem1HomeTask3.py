# Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите значение координаты оси х: '))
y = int(input('Введите значение координаты оси y: '))

if x > 0 and y > 0:
    print ("Точка координат находится в первой четверти")
if x > 0 and y < 0:
    print ("Точка координат находится во второй четверти")
if x < 0 and y < 0:
    print ("Точка координат находится в третьей четверти")
if x < 0 and y > 0:
    print ("Точка координат находится в четвертой четверти")