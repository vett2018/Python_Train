import time

N = 7
a = [0] * N #[0, 0, 0, 0, 0, 0, 0]
#print(a)

start = time.time()
for i in range(N):
    a[i] = i ** 2
finish = time.time()

print(a)

start = time.time()
b = [i ** 2for i in range(N)] #генератор списков работает быстрее чем цекл
print(b)
finish2 = time.time()
print(finish*1000)
print(finish2*1000)

"""Преобразование вводимых чисел в тип данных integer"""
d_inp = input("Целые числа через пробел: ")

a = [int(d) for d in d_inp.split()]
print(a)

""" Определение четного не четного числа в генераторе списке с использованием тернарного оператора"""
d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
d_new = ["четное" if x % 2 == 0 else "не четное"
         for x in d
         if x > 0] #дополнительное условие число больше нуля
print(d_new)