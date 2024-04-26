"""
У вас есть данные внутри последовательности, и вы хотите извлечь значения или
сократить последовательность по какому либо критерию.
"""
import math
from itertools import compress

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]


    mylist_filter = (n for n in mylist if n > 0) #выражение-генератор
    print(mylist_filter)
    for i in mylist_filter:
        print(i)

    mylist_filter_2 = [n for n in mylist if n > 0] #генератор списка
    print(mylist_filter_2)
    print('_____________________________________________________________')

    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    values_2 = ['-', 'N/A']
    ivals = list(filter(is_int, values)) #filter() создает итератор, так что если вы хотите получить список результатов, не забудьте использовать list()
    print(ivals)
    print("___________________________")

    list_gen = [math.sqrt(n) for n in mylist if n > 0] #взятие корня только у положительных элементов
    print(list_gen)
    print("_________________")
    clip_neg = [n if n > 0 else 0 for n in mylist] #замена отрицательных значений на нули
    print(clip_neg)
    print("_________________")
    """
    Две колонки данных. Создать список всех адресатов, 
    где соответвующие значения counts больше пяти
    """
    counts = [10, 30, 10, 4, 1, 7, 6, 100]
    print(counts)
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
        '5148 N CLARK',
    ]

    more5 = [n > 5 for n in counts]
    print(more5)
    p = list(compress(addresses, more5))
    print(p)



