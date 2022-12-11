# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# Пример: 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

from random import randint

player_first = input("Имя первого игрока: ")
player_second = input("Имя второго игрока: ")
value = int(input("Всего количество конфет на столе: "))

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player_first}")
else:
    print(f"Первый ходит {player_second}")

coun1 = 0 
coun2 = 0

while value > 28:
    if flag:
        k = input_dat(player_first)
        coun1 += k
        value -= k
        flag = False
        p_print(player_first, k, coun1, value)
    else:
        k = input_dat(player_second)
        coun2 += k
        value -= k
        flag = True
        p_print(player_second, k, coun2, value)

if flag:
    print(f"Выиграл {player_first}")
else:
    print(f"Выиграл {player_second}")