# Задайте список из (2*N+1) элементов, заполненных
# числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ.
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(range(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
x = open('file.txt','r')
result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(result)

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Number of elements: ', get_numbers(numbers))

x = int(input('Enter  position of first element: '))
y = int(input('Enter position of second element: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)