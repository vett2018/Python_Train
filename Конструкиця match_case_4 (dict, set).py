json_data = {"id": 55, 'type': 'list', 'data': [1,2,3], 'acces': True, 'date': '01.01.2023'}
"""Обработка словаря 
type принимает значение list тогда из data """

match json_data:
    case {'type': 'list', 'data': list() as lst}:
        print(f'JSON-данные: type-list: {lst}')
        #print(f'{url}, {method}')
    case _:
        print('другой запрос')

json_data2 = {"id": 2, 'acces': True, 'info': ['01.02.2024', {'login':'123', 'email':'email@m.ru'}, True, 1000]}
"""Обработка словаря 
проверить наличие ключа acces из ключ info выделить значение email """
match json_data2:
    case {'acces': a, 'info': [_, {'email': e}, _, _]}:
        print(f'JSON acces: {a}, email: {e}')
    case _:
        print('другой запрос')

json_data3 = {"id": 2, 'acces': True, 'info': ['01.02.2024', {'login':'123', 'email':'email@m.ru'}, True, 1000]}
print(json_data3['info'][1]['email'])

"""Множество SET"""
primary_keys = {1, 2, 3}
match primary_keys:
    case set() as keys if len(keys) == 3:
        print(keys)
    case _:
        print("другая операция")