# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

binar = ""
digit = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while digit != 0:
    binar = str(digit%2) + binar
    digit //=2
print(binar)