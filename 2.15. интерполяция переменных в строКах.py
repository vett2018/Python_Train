import sys
import string

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

class safesub(dict): # этот класс можно использовать, чтобы обернуть значения, которые подаются на вход в format_map()
    def __missing__(self, key):
        return '{' + key + '}'

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

if __name__ == '__main__':
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))
    name = 'Sasha'
    n = 35
    print(s.format_map(vars()))
    print("++++++++++++++++++")
    a = Info('Sasha Petrov', 34)
    print(s.format_map(vars(a)))

    """  File "<stdin>", line 1, in <module> KeyError: 'n' 
    Недостаток format() и format_map() в том, что они не могут аккуратно справиться с отсутствующими значениями
    """
    #s.format(name='Guido') #метод format не могут аккурато справится с отсутсвующими значениями
    print('++++++++++++++++++++++++')
    del name, n  #переменная не определена
    tmp = s.format_map(safesub(vars()))
    print(tmp)
    print('++++++++++++++++++++++++')
    name = 'Sasha'
    n = 35
    print(sub("Hello {name}"))
    print(sub('You have {n} messages.'))
    print(sub('Your favorite color is {color}'))
    print('+++++++++++++++++++++++++++++++++')
    s = string.Template('$name has $n messages.')
    
    print(s.substitute(vars()))




