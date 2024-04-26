"""n = int(input("введите целое положительное число не больше 10: "))
if n < 1 or n >= 10:
    print('Не верно введено натуральное число')
else:
    p = 1
    for i in range(1, n+1):
        p *= i

    print(f'Факториал {n}! = {p}')"""

"""Объеденить все слова в одну строку"""
words = ['Python', "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]

"""s = ""
for w in words:
    s = s + w + " "
print(s)

words2 = " ".join(words)
print(words2)"""

# name = 'Petr'
# n = 23
# s = '{name} has {n} messages.'
# #s.format_map(vars())
# s.format(name="Petr", n=23)
# print(s)

"""Двузначные числа заменить нулями"""
digs = [4, 3, 100, -53, -30, 1, 34, -8, 12]
for i in range(len(digs)):
    if 10 <= abs(digs[i]) <= 99: #abs модуль не отрицательное число
        digs[i] = 0
print(digs)

""" ТОЖЕ САМОЕ ТОЛЬКО С ФУНКЦИЕЙ ENUMERATE"""
for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:  # abs модуль не отрицательное число
        digs[i] = 0
print(digs)

""" Преобразование кирилицы в латиницу """
""" Таблица Unicode Из текущего символа вычитаетсся начальный сивол. Получаем номер (индекс)
из списка rus_alf"""

rus_alf = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
         'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
         'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
         'shch', '', 'y', '', 'e', 'yu', 'ya'
         ]
start_index = ord('а') #принимает значение для первой буквы рус. алф.
#title = 'Программирование на Python - лучший курс'
title = input("введите текст на русском языке: ")
slug = '' #хранит преобразование кирилицы в латиницу

for s in title.lower():
    if 'а'<= s <= 'я':
        slug = slug + rus_alf[ord(s)-start_index]
    elif s == 'ё':
        slug = slug + 'yo'
    # elif s in "!&?,.;:":
    #     slug = slug + '-'
    else:
        slug = slug + s #различные сиволы
print(f'Текст на латинице\n{slug}')







