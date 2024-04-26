"""Подключение к базе данных и формируется словарь вот с такими данными"""
"""Проверка для подключения к базе данных"""
def connect_db(connect: dict) -> str:
    match connect:
        case {'server': host, 'login': login, 'password': pswd, 'port': port}:
            return f'Connection:{host}@{login}.{pswd}:{port}'
        case {'server': host, 'login': login, 'password': pswd}:
            port = 24
            return f'Connection:{host}@{login}.{pswd}:{port}'
        case _:
            return "Error Connection!"

def connect_db2(connect: dict) -> str:
    match connect:
        case {'server': host, 'login': login, 'password': pswd, 'port': port}:
            pass
        case {'server': host, 'login': login, 'password': pswd}:
            port = 24
        case _:
            return "Error Connection!"

    return f'Connection:{host}@{login}.{pswd}:{port}'

request = {'server': '127.0.0.1', (1,): 67, 'login': 'root', 'password': '1234', 'port': 24}

result = connect_db2(request)
# с помощью функции connect_db выпонлять проверку данных в запросе request
# если все нормально возвращать результат подключения
print(result)
