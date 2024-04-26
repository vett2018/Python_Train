def func(x):
    def add(a):
        return x + a
    return add

test = func(100)
print(test(200))

def func2 (**args):
    return args

print(func2(a=23, b=44, c=55))
print(func2(fff = 'ddddd', gf = 555))



lambda_ = lambda x, y: x * y
print(lambda_(2,5))
print(lambda_('qwer ', 7))

print((lambda x, y: x * y)(2,6))

f = lambda *args: args
print(f(2, 56, 78.77))

lambda param: «Просто строка, но уже с обязательным аргументом param»