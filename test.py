a = input("введите имя <a> = ")
# b = int(input("введите число <b> = "))
# result = a + b
# # print(type(a))
# print(result)
if int(a) > 0:  # условие выполняется #if 0: условие не выполняется
    if int(a) > 10:
        print("Вы ввели число больше 10")
    else:
        print("Вы ввели число меньше 10 и больше 0")
elif int(a) < -10:
    print("Вы ввели число меньше -10")
else:
    print("Вы ввели число меньше 0 и больще -10")
print("All id okay")

name = input("введите имя ")
A = 'YES' if name != "Test" else 'NO'
print(A)
