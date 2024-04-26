'''Пользователь вводит два целых значения. Э будут размерности двумерного списка и его формиование'''
M, N = list(map(int, input('Введите M и N ').split()))

zeros = []
for i in range(M):
    zeros.append([0]* N)

print(zeros)

for i in range(M):
    for j in range(N):
        zeros[i][j] = 2
print(zeros)

# t = ['1', '2', '3', '4']
# print(t)
# t_new = []
# for i in range(len(t)):
#     t_new = t_new + [int(t[i])]
# print(t_new)
#
# t2 = ['2', '2', '2', '2']
# t2_new = list(map(int, t2))
# print(t2_new)
print('____________________')
"""Вложенный список двумерный список. 
Значение строк поменять на столбцы. Чтроки сделать столбцами"""
"""
1   2   3  4         1   5   9   13 
5   6   7   8   ->    2   6   10  14
9   10  11  12        3   7   11  15
13  14  15  16        4   8   12  16
Главную диагональ не трогаем
"""

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in A:
    for j in i:
        print(j, end='\t')
    print()

for i in range(len(A)):
    for j in range(i+1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]
print('Новая матрица')
for i in A:
    for j in i:
        print(j, end='\t')
    print()

