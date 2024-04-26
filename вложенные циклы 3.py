""" Заменить двойные пробелы на одинарные"""
t = ['- Скажи-ка,    дядя, ведь  не даром',
     "Москва          спаленная  пожаром",
     "Французу          отдана",
     "Ведь  были          схватки  боевые",
     "Да  говорят еще  какие",
     "Недаром       помнит        вся Россия",
     "Про день  Бородино"]
for i, line in enumerate(t):
     while line.count("  "): # метод count ищет двойной пробел в строке, если вхождений нет то условие ложное, если есть то истина
          line = line.replace('  ', ' ') # метод замены в строке
          t[i] = line #сохраняем строку в коллекции t
print(t)

"""Алтернативный вариант без цикла While"""
# for i in range(len(t)): #элементы всего списка
#      for j in range(len(t[i])): #элемента всего списка
#           count_ = t[i].count("  ") #подсчет двойных пробелов в строке
#           t[i]= t[i].replace('  ', ' ') # замена двойного пробела на одинарный
# print(t)


