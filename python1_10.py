
def dedupe(items): #функция удаления повторных элементов
    """
    Удаление дубликатов из хешируемой последовательности
    :param items: массив на вход функции
    :return: новое множество из уникальных элементова
    """
    seen = set() #создание пустого множества
    for item in items: #цикл по элементам массима
        if item not in seen: #если элемента нет в множестве
            yield item #двигаемся вперед на один жлемент
            seen.add(item) #заносим элемент в множество


def dedupe_2(items, key=None): #удаление повторных элементов из словаря
    seen = set()
    for item in items:
        val = item if key is None \
            else key(item)
        if val not in seen:
            yield item
            seen.add(val)



if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    b = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5]

    l = [{'x': 1, 'y': 2},
         {'x': 1, 'y': 3},
         {'x': 1, 'y': 2},
         {'x': 2, 'y': 4}]
    print(list(dedupe(a))) #[1, 5, 2, 9, 10]
    #print(list(dedupe(b)))  #[1, 2, 3, 4, 5]
    print(l)
    print(list(dedupe_2(l, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe_2(l, key=lambda d: (d['x']))))
    #print( list(dedupe_2(l, key=lambda d: d['x']))) #[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]