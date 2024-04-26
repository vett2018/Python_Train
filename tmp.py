from functools import reduce

def quader(*args: int) -> int:
    """
    Функция принимает на вход любое количество аргументов,
    перемножает их между собой, возводит в квадрат и
    возвращает результат в виде целочисленного числа.
    """
    return reduce(lambda x, y: x * y, map(lambda x: x * x, args))

def fibonachi(n: int) -> list:
    """
    Функция принимает на вход целочисленное число и
    строит ряд Фибоначчи, длиной равной переданному аргументу в функцию.
    """
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

print(fibonachi(quader(3,3)))