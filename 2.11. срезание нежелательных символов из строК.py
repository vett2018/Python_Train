import re

if __name__ == '__main__':
    # Срезание пробело
    s = '               hello world  '
    print(s.strip())

    # Срезание символов

    t = '-------hello====='
    print(type(t))

    tmp = t.strip('-=')
    print(tmp)
    print("+++++++++++++++++++")
    s2 = ' hello           world  \n'
    print(s2.strip())

    #tmp2 = s.replace(' ', '') #helloworld
    tmp3 = re.sub('\s+', ' ', s) #количество пробелов между словами и вконце
    print(tmp3) # hello world



