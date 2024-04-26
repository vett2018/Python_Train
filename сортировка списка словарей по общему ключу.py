from operator import itemgetter

if __name__ == '__main__':
    rows = [
        {'fname': 'Drian', 'lname': 'AJones', 'uid': 10003},
        {'fname': 'Aavido', 'lname': 'Beazley', 'uid': 102},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Cig', 'lname': 'Jones', 'uid': 14}
    ]

    rows_by_fname = sorted(rows, key=itemgetter('fname')) #сортировка в алфавитном порядке возрастания
    rows_by_uid = sorted(rows, key=itemgetter('uid')) #сортировка в порядке возрастания по uid

    print(rows_by_fname)
    print(rows_by_uid)

    #rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname')) #сортировка с двумя ключами
    #print(rows_by_lfname)

    """
    Функциональность itemgetter() иногда может быть заменена lambda-выражением
    """
    rows_by_fname = sorted(rows, key=lambda r: r['fname'])
    rows_by_lfname = sorted(rows, key=lambda r: r['uid'])
    print("______________________________________________________")
    print(rows_by_fname)
    print(rows_by_lfname)
