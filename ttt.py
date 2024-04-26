import math
def sum_(items):
    head, *tail = items
    return head + sum(tail) if tail else head

if __name__ == '__main__':
    items = [10, -7, 1, 5, 9, 200, 0, 12, - 9]
    print("длина", len(items))
    print(f'сумма = {sum_(items)}')
    min_ = items[0]
    for i in range(len(items)):
        #min_ = 0
        if items[i] < min_:
            min_ = items[i]
    print(f'минимум = {min_}')
    for k in items:
        if k < min_:
            min_ = k
    print(f'минимум = {min_}')

    math.ceil(5.2)

data = {
    "Bob": 23,
    "Charlie": 36,
    "Alice": 72,
    "Eric": 18,
    "David": 9
}

print(sorted(data.items(), key=lambda x: x[1]))

sort_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
for i in sort_data:
    print(i[0], i[1])