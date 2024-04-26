
"""Написать функцию которая выбирает значение из списка по определенному критерию (фильтру)"""
lst = [5, 3, 0, -6, 8, 10, 1]

def get_filter(a, filter_= None):
    """
    :param a: список
    :param filter: фильтр по умолчанию None
    :return:
    """
    if filter_ is None: #если параметр None то фильтр не применяем
        return a

    res = []
    for x in a:
        if filter_(x): #filter - ссылка на определенную функцию. Если функция для текущего значения из списка будет True
            #то добавлять будем значение х
            res.append(x)

    return res

r = get_filter(lst)
print(r)
r = get_filter(lst, lambda x: x % 2 == 0)
print(r)
r = get_filter(lst, lambda x: x > 0)
print(r)