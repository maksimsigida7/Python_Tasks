objekt = [23, 'word', 543, 'bot', 3, 'peace', 1234]
print(f"Сортировка списка по тексту: {list(filter(lambda x: type(x) == str, objekt))}")
print(f"Сортировка списка по числам: {list(filter(lambda x: type(x) == int, objekt))}")


