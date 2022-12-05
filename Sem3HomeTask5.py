# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

numb = int(input('Введите количество значений в списке Фибоначчи: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(numb)
print(get_fibonacci(numb))