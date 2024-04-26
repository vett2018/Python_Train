a = [(i, j)
     for i in range(3) if i % 3 == 0
     for j in range(4) if j % 2 == 0]
print(a)
"""Таблица умножения"""
b = [f'{j}*{i} = {i*j}'
     for i in range(3)
     for j in range(4) # Этот список вложен в первый список
     ]
for i in b:
    print(i)
"""Операция перевода двумерного списка в одномерный"""
matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]
          ]

a = [x
     for row in matrix
     for x in row]
print(a)
print()
"""Вложенный генератор списка"""
M, N = 4, 5
matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)
for i in matrix:
    for j in i:
        print(j, end='\t')
    print()
