d = [5, 3, 7, 10, 32]

it = iter(d)
try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("список закончился")