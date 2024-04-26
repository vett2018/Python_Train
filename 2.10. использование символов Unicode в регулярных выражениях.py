import re

if __name__ == '__main__':
    num = re.compile('\d+')
    print(re.compile('.*').match('rrrryy r78jvh ghjjhkv'))
    # ASCII-цифры
    tmp = num.match('123')
    print(tmp)

    # Арабские цифры
    tmp2 = num.match('\u0661\u0662\u0663')
    print(tmp2)

    arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
    print(arabic)

    print("++++++++++++++++++++++++++++++++++++++")
    pat = re.compile('stra\u00dfe', re.IGNORECASE)
    print(pat) #re.compile('straße', re.IGNORECASE)
    s = 'straße'
    print(pat.match(s)) #<re.Match object; span=(0, 6), match='straße'>

    print(pat.match(s.upper())) #None
    print(s.upper()) #STRASSE
