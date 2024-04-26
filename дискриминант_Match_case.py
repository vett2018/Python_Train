# print("ax^2 + bx + c")
# try:
#     a = float(input("введите значение a: "))
# except ValueError:
#     print("Введите число")
# try:
#     b = float(input("введите значение b: "))
# except ValueError:
#     print("Введите число")
# try:
#     c = float(input("введите значение c: "))
# except ValueError:
#     print("Введите число")
#
# D = b ** 2 - 4 * a * c
#
# if D < 0:
#     print(f'Дискриминант \"D\" = {D}, корней нет')
# elif D > 0:
#     x1 = (- b + D ** 1/2) / (2 * a)
#     x2 = (- b - D ** 1/2) / (2 * a)
#     print(f'Дискриминант \"D\" = {D}, x1 = {x1}, x2 = {x2}')
# else:
#     x1 = - b / 2 * a
#     print(f'Дискриминант \"D\" = {D}, x1 = {x1}')

print("ax^2 + bx + c")
try:
    a = float(input("введите значение a: "))
except ValueError:
    print("Введите число")
try:
    b = float(input("введите значение b: "))
except ValueError:
    print("Введите число")
try:
    c = float(input("введите значение c: "))
except ValueError:
    print("Введите число")

D = b ** 2 - 4 * a * c

match D:
    case int() | float() if D < 0: #переменная D является целым и вещественным
        print(f'Дискриминант \"D\" = {D}, корней нет')
    case int() | float() if D > 0:
        x1 = (- b + D ** 0.5) / 2 * a
        x2 = (- b - D ** 0.5) / 2 * a
        print(f'Дискриминант \"D\" = {D}, x1 = {x1}, x2 = {x2}')
    case int() | float() if D == 0:
        x1 = - b / 2 * a
        print(f'Дискриминант \"D\" = {D}, x1 = {x1}')
    case _:
        print("Введи числа")
