import re

if __name__ == '__main__':
    data = b'Hello World'
    print('1', data[0:5])
    print('2', data.startswith(b'Hello'))
    print('3', data.split())
    print('4', data.replace(b'Hello', b'Hello Cruel'))
    data = bytearray(b'Hello World')
    print('5', data[0:5])
    print('6', data.replace(b'Hello', b'Hello Cruel'))

    del data
    data = b'FOO:BAR,SPAM'
    #print(re.split('[:,]' ,data)) #ошибка так как шаблон в байтах
    print('7', re.split(b'[:,]', data))  # Обратите внимание: шаблон в байтах

    a = 'Hello World'
    print(a[0])
    a2 = b'Hello World'
    print(a2[1])