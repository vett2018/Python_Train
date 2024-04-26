
# fio = 'Иванов Иван Иванович'
#
# print(', '.join(fio))
# print(fio.split())
# print(', '.join(fio.split()))

# x = int(input("произведите ввод склавиатуры "))
# if x % 2 == 0:
#     print("число четное")
# else:
#     print ("число не четное")

'''


if x < 0:
    print(f'x = {x} - должно быть положительным')
elif 0 <= x <= 9:
    print(f'x = {x} - цифра')
elif 10 <= x <= 99:
    print(f'x = {x} - двузначное число')
elif 100 <= x <= 999:
    print(f'x = {x} - трехзначное число')
'''
##______________________________________

#ТЕРНАРНЫЙ ОПРЕАТОР

a = int(input("\"a\" произведите ввод склавиатуры "))
b = int(input("\"b\" произведите ввод склавиатуры "))
"""
# if a > b:
#     res = a
# else:
#     res = b

res = abs(a) if a > b else abs(b)

print(res)


s = 'python'
t = 'upper'

res2 = s.upper() if t == 'upper' else s
print(res2)
"""
"""
list_ = [1, 2, 3, a if a > b else b, 4]
print(list_)
"""
print('a - ' + ('четное' if a % 2 == 0 else "нечетное") + " число")
print('b - ' + ('четное' if b % 2 == 0 else "нечетное") + " число")
