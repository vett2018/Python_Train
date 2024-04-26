N = 1000
WIDTH, HEIGHT = 1000, 500


def my_func(lst):
    #print(WIDTH, HEIGHT)
    global N
    N = 20
    for x in lst:
        n = x + 1 + N
        print(n)

my_func([1,2,3])

print(N)
