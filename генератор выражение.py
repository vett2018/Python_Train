a = (x ** 2 for x in range(6)) #выражение генератор

print(next(a)) # 0
print(next(a)) # 1
print(next(a)) # 4
print(next(a)) # 9
print("________________")
gen = (x ** 2 for x in range(6))
for i in gen:
    print(i)
print('_________________')
for i in gen: #второй раз генератор нельзя перебрать
    print(i)
print('_________________')
list_gen = list(gen)
print(list_gen) #будет пустой список так как генератор обходится один раз
print('_________________')
##lst = list(range(1000000000000000000000000000)) # MemoryError
generat_lst = (x for x in range(1000000000000000))
lst2 = []
for i in generat_lst:
    print(i, end="  ")
    lst2.append(i)
    if i >=50:
        break
print('\n')
print(lst2)
print('_________________')
genlst = (x for x in range(10, 20))
lst3 = list(genlst) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(lst3)
print('_________________')
g = [(x for x in range(10, 20))] # в списке будет ссылка на генератор функцию 
print(g)
