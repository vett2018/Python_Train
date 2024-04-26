"""Транспонирование матрицы замена строк на столбцы """
C = [[1,2,3], [5,6,7], [9,10,11]]
print(C)
for i in C:
      for j in i:
            print(j, end='\t')
      print()

C = [[row[i] for row in C] for i in range(len(C))]
print(C)

for i in C:
      for j in i:
            print(j, end='\t')
      print()
print()

g =[u**2 for u in [x+1 for x in range(5)]]
print(g)