"""Функция имитации отпрауки электронного письма"""


def send_mail(from_name, old):
    text = f"Функция отправки письма от {from_name}! И не судите строго {old} лет"
    print(text)


def get_sqrt(x):  # вычисляет квадратный корень из положительных чисел
    # if x > 0:
    #     print(x ** 0.5)
    res = "введите положительное число" if x < 0 else x ** 0.5
    return res, x


def get_max2(x, y):  # функция определния максимального значеия двух числе
    res = x if x > y else y
    return res


def get_max3(x, y, z): # функция определния максимального значеия среди двух чисел
    res = get_max2(x, get_max2(y, z))
    return res


def even(x): #определение четного и нечетного числа
    return x % 2 == 0 #проверка на четное и нечетное значение

for i in range(1, 7):
    if even(i):
        print(i)

# a, b = get_sqrt(float(input("введите целое цисло ")))
# print(a, b)

PERIMETR = False
if PERIMETR:
    def get_rect (a, b):
        return 2 * (a + b)
else:
    def get_rect (a, b):
        return a * b



print(get_rect(1.5, 3.8))

c1 = 10
c2 = 38
c3 = 8
p2 = get_max2(c1, get_max2(c2, c3))
print(f"максимальное значение: {p2}")

p3 = get_max3(c1, c2, c3)
print(f"максимальное значение: {p3}")

