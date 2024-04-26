#cmd  = ("А.С. Пушкин", "Евгений Онегин", 200, 67, "hjkhgkj")
cmd = [1, "А.С. Пушкин", "Евгений Онегин", 200.90, 1856]

match cmd: #
    #case tuple() as book: #проверка cmd является ли cmd кортежем если да то создаем новую переменную book
    #case *c,:
    #case author, title, int() | float() as prise, *_ if len(cmd)< 10: # author, title, pride = cmd
    
    case [author, title, prise] | [_, author, title, prise, _]:
        print(f" автор = {author} заголовок = {title} цена = {prise}")
        #print(f"кортеж: {c}")
    case _, author, title, prise, year:
        print(f" Книга2  {author} заголовок = {title} цена = {prise}, год = {year}")
    case _:
        print("другая операция")






