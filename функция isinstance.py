"""Посчитать в колекции (кортеж) сумму только вещественных чисел"""
data = (4.5, 8.7, True, "книга", 8, 10, -11, [True, False])
sum1=0 #сумма вещественных чисел в кортеже
sum2 = 0
for i in data:
    if isinstance(i, float):
        sum1 = sum1 + i
print(sum1)

for i in data:
    if type(i)==int:
        sum2+=i
print(sum2)
"""С помощью функции фильтер"""
sum3 = sum(filter(lambda x: isinstance(x, float), data))
print(sum3)
"""С помощью функции фильтер целочисленные значения"""
sum4 = sum(filter(lambda x: type(x) == int, data))
print(sum4)

"""С помощью дополнительной функции"""
def get_int_num(x):
    if type(x) is int:
        return x
tmp = list()
sum5 = filter(get_int_num, data)
for i in sum5:
    tmp = tmp + [i]
print(tmp)

