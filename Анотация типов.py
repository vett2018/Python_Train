from typing import Union, Optional, Any, Final, Callable


MAX_VALUE: Final = 1000
MAX_VALUE = 200  # информационная аннотация о том что переменная не может быть изменена

cnt: int = 2.8  # Элемент анотации типов данных
print(cnt)

digit = int | float
Str = Optional[str]  # Алиас в Optional добавляется None по умолчанию.
Str_2 = Union[str, None]  # Union равнозначен Optional
print(Str)

def mul2(x: Union[int, float], y: Union[int, float] = 2) -> Union[int, float]:
    return x * y


def show_x(x: Any, descr: Optional[str] = None) -> None:
    if descr:
        print(f'{descr} {x}')
    else:
        print(f'x = {x}')


res = mul2(5, 5)
print(res)
print(mul2.__annotations__)
print(show_x.__annotations__)
show_x(5.876)

"""Анотация для типов данных список, колекция, кортеж, словарь"""
lst: list[int] = [1, 2, 3] #корректно
addr: tuple[int, str] = (1, '3')

book: tuple[str, str, int] #группируем с помощью кортежей данные
book = ("Пушкин А.С.", "Евгений Онегин", 200)

elems: tuple[float, ...] #в кортеже сколько бы лементов не было будет тип Float
elems = (1.0, '1.0')
elems = (1.0, )

words: dict[str, int] = {'one': 1, 'two': 2}

words: dict[str, bool] = {'one': 1, 'two': "2"}
"""_____________________________________________________"""
def get_positive(digits: list[Union[int, float]] = None) -> list[Union[int, float]]:
    if digits:
        return list(filter(lambda x: x > 0, digits))
    return []

print(get_positive([1,2,3,4, 0, -10]))


#Callable [[TypeArg1, TypeArg2, ...], ReturnType]

def get_digits(flt: Callable[[int], bool], lst: list[int]= None) -> list[int]:
    """
    :param flt: ссылка на функцию
    :param lst: список
    :return:
    """
    if lst is None:
        return []
    return list(filter(flt, lst))

def even(x: int):
    #проверка четности элементов
    return bool(x % 2 == 0)


#Callable [[TypeArg1, TypeArg2, ...], ReturnType]
def hello_callable():
    print("Hello Callable")
#Callable [[], None]

print(get_digits(lambda x: x % 2 == 0, [1,2,3,4,5,6,7]))
print(get_digits(even, [1,2,3,4,5,6,7]))






