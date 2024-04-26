a = ['2', [1,2,3], {1: 56}, 1]

b = all(a)
print(b)
"""реализация функции all вручную"""
all_res = True
for x in a:
    all_res = all_res and bool(x)
"""Если хотя бы один элемент ложный даст на выходе False"""
print(all_res)
print("_______")
"""Функция any"""
g = [False, False, True]
print(any(g))
print("_______")
"""реализация функции any в ручную"""
#g1 = [0, 1, 2.5, 'python', [1], [1,2,3]]
g1 = [0, 0, 0, False, [1], {}]
any_res = False
for x in g1:
    any_res = any_res or bool(x)
print(any_res)
"""Крестики нолики проверка функцией all()
x   x   x
0   x   0
x   x   x
проверка столбцов диагоналей и строк
"""
krst = ['x','x','x','0','x','0','x','x','x']
def true_x(a):
    #проверка истенности а = Х или 0
    return a == "x"
row_1 = all(map(true_x, krst[:3]))
row_2 = all(map(true_x, krst[3:6]))
row_3 = all(map(true_x, krst[6::]))

print(row_1, row_2, row_3)

colb_1 = all(map(true_x, krst[::3]))
colb_2 = all(map(true_x, krst[1::3]))
colb_3 = all(map(true_x, krst[2::3]))

print(colb_1, colb_2, colb_3)

diag_1 = all(map(true_x, krst[::4]))
diag_2 = all(map(true_x, krst[2:7:2]))
print(diag_1, diag_2)
"""Игра сапер 10 на 10 состоит из нулей. Представление будет в одном списке
в индексе 4 у нас мина *. Если пользователь в иговом поле пользователь наступил на мину то он проиграл
Проверка с проигрышем функцией any"""
N = 10
P = [0] * (N*N)
P[4] = '*'
print(P)
loss = any(map(lambda x: x == '*', P))
print(loss)

print(39245344344343434324343724e-15)