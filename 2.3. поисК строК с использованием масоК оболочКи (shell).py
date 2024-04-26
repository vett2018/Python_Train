from fnmatch import fnmatch, fnmatchcase

if __name__ == '__main__':

    pp = fnmatch('foo.txt', '*.txt') #* - захват множества символов
    print(pp)

    pp2 = fnmatch('foo.txt', '?oo.txt') #? - захват одного символа
    print(pp2)

    pp3 = fnmatch('Dat45.csv', 'Dat[0-9]*')
    print(pp3)

    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    ll = [name for name in names if fnmatch(name, 'Da*.csv')]
    print(ll)

    "через цикл for сортировка данных произошла"
    new_names = list()
    for i in names:
        if fnmatch(i, 'Da*.csv'):
            new_names.append(i)
    print(new_names)

    ll3 = [name for name in names]
    print(ll3)

    PP = fnmatch('foo.txt', '*.TXT')
    print(PP)
    print("______________________________________")
    addresses = ['5412 N CLARK ST',
                 '1060 W ADDISON ST',
                 '1039 W GRANVILLE AVE',
                 '2122 N CLARK ST',
                 '5454 N CLAKS ST',
                 '4802 N BROADWAY',
                 ]
    print(addresses)
    new_addresses = [addr for addr in addresses if fnmatchcase(addr, '*ST')]
    print(new_addresses)
    new_addresses2 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
    print(new_addresses2)


