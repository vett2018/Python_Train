import random

x = random.random()
print(x)
x = random.uniform(1, 1000)
print(x)
x = random.randint(1, 1000)
print(x)
x = random.randrange(1, 100, 2) #не четные
print(x)

x = random.gauss(0, 3.5)
print(x)
"""Есть список и мы хоти выбрать из него один элемент случайным образом"""
lst = [4, 5, 0, 'python', 10, 76, 3]
a = random.choice(lst)
print(f'случайный элемент из списка = {a}')
print(f'случайный элемент из списка = {lst[random.randint(0, len(lst))-1]}')

"""Есть список и мы хоти перемешать все элементы между собой"""

lst_shuffle = random.shuffle(lst)
print(lst_shuffle)


