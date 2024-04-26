from collections import defaultdict

if __name__ == '__main__':
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    min_price = min(zip(prices.values(), prices.keys())) #(10.75, 'FB')
    max_price = max(zip(prices.values(), prices.keys())) #(612.78, 'AAPL')

    prices_sorted = sorted(zip(prices.values(), prices.keys())) #[(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]
    print(prices_sorted)

    print(min(prices)) # Вернет 'AAPL'
    print(max(prices)) # Вернет 'IBM'

    print(min(prices.values()))  # Вернет 10.75
    print(max(prices.values()))  # Вернет 612.78

    print(min(prices, key=lambda k: prices[k]))  # Вернет 'FB'
    print(max(prices, key=lambda k: prices[k]))  # Вернет 'AAP

    a = {
        'x': 1,
        'y': 2,
        'z': 3,
        'gg': 11,
        'll': 66,
        'cc': 88
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2,
        'gg': 55,
        'qq': 111,
        'cc': 88
    }

    print(a.keys() & b.keys()) # {'y', 'gg', 'x'} поиск общих ключей
    print(a.keys() - b.keys()) # {'z', 'll'} # Находим ключи, которые есть в a, но которых нет в b
    print(a.items() & b.items()) # {('cc', 88), ('y', 2)} #Находим общие пары (key,value)

    # Создаем новый словарь, из которого удалены некоторые ключи
    c = {key: a[key] for key in a.keys() - {'x', 'y', 'll', 'cc', 'yt', 'gjgjgjg'}} # c – это {'gg': 11, 'z': 3}
    print(c)
    print("_____________________")
    print(b.keys())
    print(b.items())
    print(b.values())
    "Конструирование словарей"
    # d = {}
    # for key, value in range(1, 11):
    #     if key not in d:
    #         d[key] = []
    # d[key].append(value)
    #
    # print(d)

    #d = defaultdict(list)
    #for key, value in pairs:
    #    d[key].append(value)
