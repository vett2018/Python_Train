from operator import itemgetter
from itertools import groupby

from collections import defaultdict


if __name__ == '__main__':
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '3333 W GRANVILLE', 'date': '04/04/2014'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        {'address': '4444 W GRANVILLE', 'date': '04/04/2014'},
    ]

    # #Сначала сортируем по нужным полям
    # rows.sort(key=itemgetter('date'))
    #
    # #Итерируем в группах
    # for date, items in groupby(rows, key=itemgetter('date')):
    #     print(date)
    #     for i in items:
    #         print("   ", i)

    print("__________________________________________________________")
    """
    сгруппировать данные вместе в крупную структуру
    данных с произвольным доступом
    """
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

    print(rows_by_date)

    for r in rows_by_date['04/04/2014']:
        print(r)


