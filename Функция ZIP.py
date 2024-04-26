a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = 'python'

z = zip(a, b, c) #z = list(zip(a, b, c))


for i, i2, i3 in z:
    print(i, i2, i3)
"""Присваивание"""
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = 'python'
z1, z2, z3, z4 = zip(a, b, c)
print(z1, z2, z3, z4) #(1, 5, 'p') (2, 6, 'y') (3, 7, 't') (4, 8, 'h')
z1, *z2 = zip(a, b, c)
print(z1, z2) #(1, 5, 'p') [(2, 6, 'y'), (3, 7, 't'), (4, 8, 'h')]
print("_____________")
"""Преобразование с помощбю zip"""
z1 = list(zip(a, b, c))
print(*z1)
t1 ,t2, t3 = zip(*z1)
print(t1 ,t2, t3, sep='\n')