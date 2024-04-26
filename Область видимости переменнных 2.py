x = 0


def outer():
    x = 1
    """Здесь нельзя обращаться по nonlocal Х  так как "выше" 
    уже глобальная область видимости"""
    def inner():
        nonlocal x
        x = 2
        print("inner: ", x)

    inner()
    print("outer: ", x)

outer()
print("global: ", x)