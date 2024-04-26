request = {"id": 55, 'url': 'https://hello.com', 'method': 'GET', 'timeout': 1000, 'date': '07.12.2023'}


match request:
    #case {'url': str() as url, 'method': str(method), 'timeout': 1000 | 1001}: #этот шаблон каждый раз отрабатывает когда поступает шаблон
    case {'url': url, 'method': method, **kwarg}:
        print(f'Запрос: URL: {url}, method: {method}')
        #print(f'{url}, {method}')
    case _:
        print('другой запрос')


# r = {'url':'https://hello.com', 'method': 'GET', 'timeout': 1000}
# print(r['url'], r['method'])


