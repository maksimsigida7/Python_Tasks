# Напишите программу которая будет на вход принимать
# чисто N а выводить числа от -N до N

num  = int(input('Введите число: '))
numbers = [i for i in range(-num,num + 1)]
print (numbers)

# Второй вариант

num1 = int(input('Введите число\n'))
if num1 > 0:
    for i in range(-num, num + 1):
        print(i, end=" ")

else:
    for i in range(num, -num + 1):
        print(i, end=" ")