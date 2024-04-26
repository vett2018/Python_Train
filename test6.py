d = {'test': 1, 'test_2': 'TeST'}
#print(d['test_2'])
print(d)
d2 = dict(short='dict',longer ='dictionary', c =3)
d2['short']=2334
print(d2)




dict_sample = dict([(23,34), ('gggg', 55)])
print("111111111",dict_sample)

d3 = dict.fromkeys(['a', 'b', 'c'], 1)
print(d3)

dict_ ={a: a ** 2 for a in range(7)}
print(dict_)

person = {'name': {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'}, 'address': ['г. Андрюшкин', 'ул. Васильковская д.23б', 'в.122'],
          'phone': {'home_phone': '233-3233', 'mobile_phone': '8-911-234-23-12', 'moile_phone_2': 'нет'}}
print(person['phone']['home_phone'])
print(person['address'][1])

print(person.keys())
print(person.values())



