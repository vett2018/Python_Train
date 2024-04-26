import unicodedata

if __name__ == '__main__':
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print(s1) #Spicy Jalapeño
    print(s2) #Spicy Jalapeño
    print(ascii(s1)) #'Spicy Jalape\xf1o'
    print(ascii(s2)) #'Spicy Jalapen\u0303o'
    print(s1 == s2)
    print(len(s1)) #14
    print(len(s2)) #15
    print("++++++++++++++++++++++++")
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print(t1 == t2)
    print(ascii(t1)) #'Spicy Jalape\xf1o'

    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)
    print(t3)
    print(ascii(t3)) #'Spicy Jalapen\u0303o'
    print("++++++++++++++++++++++++")
    s = '\ufb03'  # Один символ
    print(s) #ﬃ


    t5 = unicodedata.normalize('NFD', s)
    print(t5) #ﬃ
    print(ascii(t5))

    # Обратите внимание на разбивку объединенных букв
    t6 = unicodedata.normalize('NFKD', s)
    print(t6) #ffi
    print("ASCII", ascii(t6)) #ASCII 'ffi'


    t7 = unicodedata.normalize('NFKC', s)
    print(t7) #ffi
    print("ASCII", ascii(t7))  # ASCII 'ffi'

    t8 = unicodedata.normalize('NFD', s1)
    print(t8)
    print(type(t8))
    print("++++++++++++++++++++++++++")

    print("".join(c for c in t8 if not unicodedata.combining(c))) #Spicy Jalapeno
    """
    через цикл
    """
    str_ = ''
    # print(type(str_))
    for c in t8:
        if not unicodedata.combining(c):
            str_ = str_ + f'{c}'
    print("через цикл", str_)
    print("++++++++++")







