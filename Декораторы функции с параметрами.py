"""Создаем декоратор для вычисления произвольной функции"""
import math


def df_decorator(dx=0.01):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            # dx = 0.0001
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper
    return func_decorator

#@df_decorator(dx=0.1)
def sin_df(x):
    return math.sin(x)

f = df_decorator(dx=0.0001) #декорирование стандартным способом
sin_df = f(sin_df)

df = sin_df(math.pi / 3)
print(df)
