"""Преобразовать список в множество, которое состоит из чисел, ИСПОЛЬЗУЯ ГЕНЕРАТОР СЛОВАРЯ"""
d = [1, 2, '1', '2', -4, 3, 4]
a = {int(x) for x in d}

print(a)

set_d = set()
for i in d:
    set_d.add(int(i))
    # a = int(i)
    # set_d.add(a)
print(set_d)
"""Сделать ключи словаря с заглавной буквы, а значения сделать INT"""
m = {"неудовл.": 2, "удовл.": 3, "хорошо": '4', "отлично": '5'}
m2 = {}
for key, val in m.items():
    # key = i.upper()
    # val = int(k)
    #m2[key] = val
    m2[key.upper()] = int(val)
print(m2)
"""C ПОМОЩЬЮ ГЕНЕРАТОРА СЛОВАРЯ"""
m3 = {key.upper():int(val) for key, val in m.items()}
print(m3)
"""Преобразовать в можество которое состоит из положительных числе с помощью генератора множества"""
d = [1, 2, '1', '2', -4, 3, 2, 4]
f = {int(x) for x in d if int(x) > 0}
print(f)

"""Поменять ключи и значения друг с другом местами. При этом выбрать значения словаря от 2 до 5"""
x = {"очень плохо.": 0, "плохо.": 1, "неудовл.": 2, "удовл.": 3, "хорошо": '4', "отлично": '5'}
print(x)
x2 = {}
for key,value in x.items():
    if 2 <= int(value) <= 5:
        x2[value] = key
print(x2)

"""C помощью генератора словаря"""
c = {int(value): key for key,value in x.items() if 2 <= int(value) <= 5}
print(c)


