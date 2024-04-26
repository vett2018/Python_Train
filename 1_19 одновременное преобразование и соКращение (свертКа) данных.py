import os

nums = [1, 2, 3, 4, 5]

s = (x * x for x in nums)
# for t in s:
#     print(t)
s2 = sum([x * x for x in nums])
print(s2)

if __name__ == '__main__':

    # Определяем, есть ли файлы .py в каталоге
    files = os.listdir("C:/Users/admin/Desktop/DevPyQt-master")
    if any(name.endswith('.py') for name in files):
        print('There be python!' )
    else:
        print('Sorry, no python.')

    # Выводит кортеж как CSV
    ss = ('ACME', 50, 123.45)
    print(ss)
    print(','.join(str(x) for x in ss))

    # Сокращение (reduction) данных по полям в структуре данных

    portfolio = [
        {'name': 'GOOG', 'shares': 50},
        {'name': 'YHOO', 'shares': 75},
        {'name': 'BOL', 'shares': 20},
        {'name': 'SCOX', 'shares': 65}
    ]
    min_shares = min(s['name'] for s in portfolio)
    print(min_shares)

    # Изначальный: возвращает 20
    min_shares2 = min(s['shares'] for s in portfolio)
    print(min_shares2)
