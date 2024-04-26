from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
Subscriber(addr='jonesy@example.com', joined='2012-10-19')

print(sub.addr)

print(sub.joined)

print(len(sub))


def compute_cost(records): #бычные кортежи
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

def compute_cost2(records): #именованные кортеж
    total = 0.0
    for rec in records:
        s= Stock(*rec)
        total += s.shares * s.price
    return total

if __name__ == '__main__':
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])
