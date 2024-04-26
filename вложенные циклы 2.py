a = []
b = []
c = []
mas_row_a = int(input("Введите колличество строк массива А: "))
mas_col_a = int(input("Введите колличество столбцов массива А: "))

for i in range(mas_row_a):
    a = a + [[]] #a.append([])
    for j in range(mas_col_a):
        a[i] = a[i] + [int(input(f"введите элемент массива [{i}][{j}] = "))] #a[i].append(input(f"введите элемент массива [{i}][{j}] = "))
print(f'Массив А имеет вид\n{a}')

mas_row_b = int(input("Введите колличество строк массива B: "))
mas_col_b = int(input("Введите колличество столбцов массива B: "))
for i in range(mas_row_b):
    b = b + [[]] #a.append([])
    for j in range(mas_col_b):
        b[i] = b[i] + [int(input(f"введите элемент массива [{i}][{j}] = "))] #a[i].append(input(f"введите элемент массива [{i}][{j}] = "))
print(f'Массив B имеет вид\n{b}')

# if len(b) != len(a[0]):
#     print('Вычисления над матрицами невозможны')
# else:
for row in range(len(a)): #пробегаем по индексам списка 0 -> 1 -> 2
    r = []  # список для формирования строки которая содержит сумму вложенных списков a и b
    for j in range(len(a[row])): # пробегаем по внутрненнему списку 0 -> 1 -> 2 -> 3
        res = a[row][j] + b[row][j]
        r = r + [res] #r.append(res) аналог
    c = c + [r] # c.append(r)
print(f'Массив C имеет вид\n{c}')

"""Через функцию ENUMERATE"""
for i, row_a in enumerate(a):
    r = []
    for j, x_el in enumerate(row_a):
        r = r + [x_el + b[i][j]]
    c = c + [r]  # c.append(r)
print(f'Массив C имеет вид\n{c}')

