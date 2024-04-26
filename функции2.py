
def get_v(a, b, c, verbose = True):
    """
    Расчет объема прямоугольного паралепипеда
    :param a: губина
    :param b: ширина
    :param c: высота
    :return: объем прямоугольного паралепиида
    """
    if verbose: # if verbose == True
        print(f"a = {a}, b = {b}, c = {c}")
    res = a * b * c
    return res

D = "  LGJDGJD" \
    "KDLG   KLDKGKG   "
v = get_v(1, 2, 3, True)
print(f'Объем прямоугольного паралепипеда: {v}')

"""Функция срванивает две строки между собой
с учетом и без учета регистра
учет пробела до и после в строке"""
def cmp_str(s1, s2, reg, trim=True):
    """
    Функция учета регистра двух строк
    :param s1: ссылка на строку 1
    :param s2: ссылка на строку 2
    :param reg: флаг учета регистра ( формальный параметр)
    :param trim: флаг учета пробела и других символов в строке (формальный параметр)
    :return:
    """
    if reg: #если флаг равен true
        s1 = s1.lower()
        s2 = s2.lower()
    if trim: #если флаг равен true
        s1 = s1.strip() #метод strip удаляет пробелы и переносы
        s2 = s2.strip()

    return s1 == s2

s1 = str(input("введите строку s1: "))
s2 = str(input("введите строку s2: "))
regfl = int(input("приравнять к нижнему регистру строки при проверке 0-нет, 1-да "))
trimfl = int(input("удалить лишние пробелы при проверке строк 0-нет, 1-да "))

res = cmp_str(s1, s2, reg=regfl, trim=trimfl)
print(res)
#res = cmp_str("Python", " Python")
#print(res)