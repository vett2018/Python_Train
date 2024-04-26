book_1 = ('Пушкин', 'Евгений Онегин', 1843)
book_2 = ['Толстой', "Война и мир", 1756, 2345.24]
book_3 = {'author': 'Толстой', 'title': "Анна Каренина", "year": 2020}
book_4 = {'author': 'Замятин', 'title': "Мы", "year": 2020, 'price': 755}

"Сформировать функцию которая на выходе формирует кортеж в виде автор, название, год, цена" \
"Если нет одного из начений то вывести на"
#дополнительная проверка на чилочесленный тип переменной year

def book_to_tuple(data: dict | tuple | list, min_year =1800, max_year = 2024) -> tuple | None:
    price = None
    match data:
        case author, title, int(year)  if min_year < year < max_year: #шаблон предположения списка или кортежа
            pass
        case author, title, int(year), price, *_:
            pass
        case {'author': author , 'title': title, "year": int(year), 'price': price}:
            pass
        case {'author': author, 'title': title, "year": int(year)}:
            pass
        case _:
            return None

    if not (min_year < year < max_year):
        return None
    return author, title, year, price

tmp_book1 = book_to_tuple(book_1)
tmp_book2 = book_to_tuple(book_2)
tmp_book3 = book_to_tuple(book_3)
tmp_book4 = book_to_tuple(book_4)
print(tmp_book1, tmp_book2, tmp_book3, tmp_book4, sep='\n')