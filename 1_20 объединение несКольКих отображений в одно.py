from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a,b)
print(c['x']) # Выводит 1 (из a)
print(c['y']) # Выводит 2 (из b)
print(c['z']) # Выводит 3
print()
values = ChainMap()
print(values)
values['x'] = 1
print(values)
# Добавляем новое отображение
values = values.new_child()
values['x'] = 2
print(values)
# Добавляем новое отображение
values = values.new_child()
values['x'] = 3
print(values)
# Удаляем последнее отображение
values = values.parents
values['x']
print(values)
# Удаляем последнее отображение
values = values.parents
values['x']
print(values)
print()
d = {'x': 1, 'z': 3}
c = {'y': 2, 'z': 4}
merged = dict(c)
merged.update(d)
print(merged)
print("______________")
d['x'] = 13
merged['x']
merged.update(d)
print(merged)
print('ключ y:', merged['y'])
print("______________")
dd = {'x': 1, 'z': 3}
cc = {'y': 2, 'z': 4}
merged = ChainMap(dd, cc)
merged['z'] #print(merged['z']) # 3
dd['xx'] = 42
#merged.update()
print(merged)
