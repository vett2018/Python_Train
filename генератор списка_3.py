A = [[a for a in range(3)]for b in range(4)]
print(A)
"""__________________________"""
AA = [a
      for a in range(3)
      for a in range(4)]
print(AA)
"""__________________________"""
print()
B = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

B1 = [[x ** 2 for x in row] for row in B]
print(B1)
"""__________________________"""
B2 = [b ** 2
      for row in B
      for b in row]
print(B2)
print()

