a = ['1', '2', '3', '4', '5']

b = map(int, a) #АНАЛОГ b = (int(x) for x in a)

c = []
for i in range(len(a)):
    #print(next(b))
    c.append(next(b))
print(c)



cities = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]
'''С помощью map сформируем последовательность длины названия городов'''
cities = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]

def symbols(word): #aункция symbols перевода в нижний регистр
    return word.upper()

#cities_gen = map(len, cities) #подсчет длины каждого слова в списке
#cities_gen = map(str.upper, cities) #перевод в верхний регистр
#cities_gen = map(symbols, cities) #вызов функции symbols перевода в нижний регистр
#cities_gen = map(lambda x: x.upper(), cities) # через лямбду функцию
cities_gen = map(lambda x: x[::-1].upper(), cities)

cities_list = list(cities_gen) # длина каждого слова в списке

print(cities_list)

print('_______________________')
s = list(map(str, input("ввод: ").split()))
print(s)



