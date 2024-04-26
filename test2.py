i = 0
while i <= 10:
    print(i)
    i += 2

"цикл for проходит по строке по списку, словарю"

for j in 'hello world':
    if j == 'a':
        #continue #пропуск итерации
        break #выход из цикла
    print(j * 2, end= "")
else: "else используется для break"
    print("Буквы а нет в слове")
