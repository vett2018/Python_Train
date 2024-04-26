"""РЕКУРСИВНАЯ ФУНКЦИЯ ИДЕТ СНАЧАЛА В ГЛУБИНУ
 ПОТОМ ВОЗВРАЩАЕТСЯ ОБРАТНО"""
def recurcive(value):
    print(value)
    if value < 4:
        recurcive(value + 1)
    print(value)

recurcive(1)
print("----------------------------------------------")

"""Вычисление факторила натурального числа. Вычисление происходит по рекурсии"""

def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n-1)

p = fact(5)
print(p)