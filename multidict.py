from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(list)  # мультисловарь
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(3)
    # print(d)
    # print(f'список = {d.items()}')

    c = defaultdict(set)  # мультисловарь
    c['a'].add(1)
    c['a'].add(2)
    c['b'].add(4)
    # print(c)
    # print(f'множество = {d.items()}')

    a = {}  # Обычный словарь
    a.setdefault('a', []).append(1)
    a.setdefault('a', []).append(2)
    a.setdefault('b', []).append(4)

    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = []
    d[key].append(value)
    #
    # defaultdict приводит к более чистому коду
    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)
