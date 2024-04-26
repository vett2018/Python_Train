def decorator(func):
    def wrapper():
        print("код до выполнении функции")
        func()
        print("код, который сработал после функции")
    return wrapper

def test(func):
    def wrapper():
        print("код до выполнении функции 2")
        func()
        print("код, который сработал после функции 2")
    return wrapper

@decorator
@test
def show():
    print("Я обычная функция")

show()
#dec = decorator(show)
#dec()