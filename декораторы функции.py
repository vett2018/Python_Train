#Декораторы функции
def func_decorator(func):
    """
    Функция декоратор которая принимает ссылку на некую функцию
    :param func: ссылка на функцию
    :return:
    """
    def wrapper(*args, **kwargs):
        """Внутренняя функция которая может выполнить некие операции до вызова функции func() """
        print("------------------что-то делаем перед вызовом функции")
        res = func(*args, **kwargs)
        print("-------------------что-то делаем после вызова функции")
        return res

    return wrapper



def some_func(title, tag):
    print(f"вызов  функции some_func с параметром title = {title} и tag = {tag}")
    return f"<{tag}>{title}</{tag}>"

some_func = func_decorator(some_func) #f -ссылается на внутреннюю функцию wrapper
                    # "some_func"-является аргументов ссылкой на функцию some_func()
res = some_func({12,5,5,5,5,5}, '1строка1')
print(res)



"""Равносильно что написано выше """
#f= func_decorator(some_func)
#f()





