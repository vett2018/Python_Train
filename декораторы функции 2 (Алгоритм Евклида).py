#Декораторы функции
import time


def test_time(func): #Функция тстироващик
    """
    Функция декоратор которая принимает ссылку на некую функцию
    :param func: ссылка на функцию
    :return:
    """
    def wrapper(*args, **kwargs):
        """Внутренняя функция которая может выполнить некие операции до вызова функции func() """
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et-st
        print(f"Время работы: {dt} сек")
        return res

    return wrapper

def get_fast_nod(a, b):
    """
    Быстрый алгоритм Евклида
    :param a:
    :param b:
    :return:
    """
    if a < b: #меняем местами максимальное и минимальное число (Делаем а-макс.)
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a #Наибольший делитель евклида

@test_time #функция get_node задекорирована  - декоратором test_time
def get_nod(a, b):
    """
    Функция реализует медленный алгоритм евклида между двумя числами
    :param a: число
    :param b: число
    :return:
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a #Неважно что возвращать так как a = b


#get_nod = test_time(get_nod) # декорирование функции медленный алгоритм евклида
#[!] декорировать не нужно так как уже задекорирована функция
get_fast_nod = test_time(get_fast_nod)# декорирование функции быстрый алгоритм евклида

res = get_nod(2, 1000000)
res2 = get_fast_nod(2, 1000000)

print(res, res2)




