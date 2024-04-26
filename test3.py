l = []
b = [24, 67]
list_ = [1,56, 'x', 34, 2.34, ['S','t', 'r', 'o', 'k', 'a']]
print(list_)

a = [a+b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

l.append(23)
l.append(34) #обавление списка
l.extend(b) #расширение списка
l.insert(1, 5000)
l.append(34)
l.remove(34)
l.pop(0)
print(l.index(5000))
print(l.count(5000))
l.sort()
l.reverse()
l.clear()

print(l)