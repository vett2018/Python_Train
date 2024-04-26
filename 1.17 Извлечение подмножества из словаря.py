
print()

if __name__ == '__main__':
    prices = {
        'GAZP': 167.45,
        'SPBE': 79.14,
        'ALR': 69.90,
        'LUK': 500,
        'FB': 10.75,
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
    }
    new_dict = {}
    p = prices.items()
    for key, val in prices.items():
            if val > 200:
                t = key, val
                # print(t)
                new_dict[key] = val
    print(new_dict)



    print()
    # Создать словарь всех акций с ценами больше 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    print('p1:', p1)

    # Создать словарь акций технологических компаний
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    print('p2:', p2)

    #второй вариант p2
    p2_2 = {key: prices[key] for key in prices.keys() & tech_names}
    print('p2_2:', p2_2)

    p3 = dict((key, value) for key, value in prices.items() if value > 200)
    print('p3:', p3)

