# for i in range(1, 4):
#     for j in range(1, 6):
#         print(f'i = {i}, j = {j}', end=' ')
#     print()

"""
a = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
for row in a:
    print(row, type(row), end= " ")
    for row_in in row:
        print(row_in, type(row_in), end= " ")
    print()"""

"""mas_el = int(input("Введите колличество элементов массива: "))
mas = []
for i in range(mas_el):
    mas = mas + [input(f"введите элемент {i} массива = ")]
    #mas.append(input(f"введите элемент {i} массива = "))
print(mas)"""

""" Сложение двух элементов массива с сохранением в переменную С"""
a = [[1,1,1,1], [2,2,2,2], [2,2,2,2]]
b = [[1,1,1,1], [2,2,2,2], [3,3,3,3]]


c = [] # новый массив
# for i, row in enumerate(a):
#     r = [] # список для формирования строки которая содержит сумму вложенных списков a и b
#     for j, x in enumerate(row):
#         r.append(x + b[i][j])
#     c.append(r)
#
# print(c)


for row in range(len(a)): #пробегаем по индексам списка 0 -> 1 -> 2
    r = []  # список для формирования строки которая содержит сумму вложенных списков a и b
    for j in range(len(a[row])): # пробегаем по внутрненнему списку 0 -> 1 -> 2 -> 3
        res = a[row][j] + b[row][j]
        r = r + [res] #r.append(res) аналог
    c = c + [r] # c.append(r)
print(c)











