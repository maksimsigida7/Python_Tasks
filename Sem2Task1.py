# Напишите программу которая будет принимать на вход дробь
# и показывать первую цифру бробной части

decimal = (input('Введите дробное число: '))
if ',' in decimal:
    decimal_part = decimal.split(',')[1]
    first_digit = decimal_part[:1]
    print(first_digit)
elif '.' in decimal:
    decimal_part = decimal.split('.')[1]
    first_digit = decimal_part[:1]
    print(first_digit)
else:
    print ('Число не дробное')