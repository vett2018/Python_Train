try:
    x = int(input('x: '))
except ValueError:
    print('вы ввели не число')
try:
    y = int(input('y: '))
except ValueError:
    print('вы ввели не число')
try:
    res = x / y
except ZeroDivisionError:
    print('делить на ноль нельзя')
except NameError:
    print("вы ввели не число")
try:
    print(res)
except NameError:
    print("ре зультат не может быть посчитан")
# try:
#     x = int(input())
# except ValueError:
#     print('Вы ввели не число')
