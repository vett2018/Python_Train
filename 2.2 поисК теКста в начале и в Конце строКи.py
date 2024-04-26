import os
from urllib.request import urlopen
import re

def read_data(name):
    if name.endswith(('.py', 'https:', 'ftp:', '.txt')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


if __name__ == '__main__':

    filename = 'spam.txt'

    f = filename.endswith('.txt')
    print(f)
    f2 = filename.startswith('file:')
    print(f2)

    url = 'http://www.python.org'
    u = url.startswith('http:')
    print(u)

    filenames = os.listdir('.')
    print("1111", filenames)

    print("________________________")
    "вывод текущих файлов директории по расширению файла .txt -- listcomprehesion"
    filenames2 = [name for name in filenames if name.endswith(('.txt'))]
    print(filenames2)

    print("________________________")
    "вывод текущих файлов директории по расширению файла .txt -- классический вывод"
    files_ = []
    for ff in os.listdir():
        if ff.endswith('.py'):
            files_.append(ff)

    print(files_)
    print("__________")
    print(any(name.endswith('.py') for name in filenames))

    choices = ['http:', 'ftp:']
    #url.startswith(choices) #выдаст ошибку что требуется переконвектировать в кортеж
    dd = url.startswith(tuple(choices))
    print("dd=", dd)
    print("__________")
    # окончания и префиксы через срезы
    filename_srez = "tytyty.txt"
    ff = filename_srez[-4:] == '.txt'
    print(ff)
    url_srez = 'http://www.python.org'
    gg = url_srez[:5] == 'http:' or url_srez[:6] == 'https:'
    print(gg)
    print("__________")
    # регулярные выражения
    url_re = 'http://www.python.org'
    jj = re.match('http:|https:|ftp:', url)
    print(jj)
    print("______________")



    #filenames2 = [name for name in filenames if name.endswith(('.txt'))]
    filenamesZ = os.listdir('.')
    print("1111", filenamesZ)















