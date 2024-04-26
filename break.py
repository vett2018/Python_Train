"""pass_true = 'password'
ps = None

while ps != pass_true:
    ps = input("введите пароль: ")
print('вы вошли в систему')

N = 20
i = 1

while i <= N:
    if i % 3 == 0:
        print(i)
    i = i+1"""

print("запуск цикла")

"""i = 0
while True:
    i = i + 1
    print(i)
    if i == 10:
        print('выход из цикла')
        break
print("Завершение цикла")"""

d = [1, 5, 7, 6, 0]
fndFlag = None  # флаг для поиска первого четного числа
i = 0
while i < len(d):
    print(i)
    fndFlag = d[i] % 2 == 0
    if fndFlag == True:
        break
    i += 1
print(f'значение флага = {fndFlag}, элемент списка = {d[i]}')
