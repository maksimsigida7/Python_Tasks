# Напишите программу которая принимает на вход два числа
# а на выходе выдает является ли одно из числел друг другу квадратом


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a == b**2 or b == a**2:
    print (True)
else:
    print ('False')
