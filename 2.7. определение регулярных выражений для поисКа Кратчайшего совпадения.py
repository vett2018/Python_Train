import re

if __name__ == '__main__':
    str_pat = re.compile(r'\"(.*)\"') #жадный квантификатор
    text1 = 'Computer says "no."'
    tmp = str_pat.findall(text1)
    print(tmp) #['no.']

    text2 = 'Computer says "no" Phone says "yes"'
    tmp2 = str_pat.findall(text2)
    print(tmp2) #['no." Phone says "yes.']
    print("++++++++++++++++++++++++++++++++++++++++")
    str_pat = re.compile(r'\"(.+?)\"') #ленивый квантификатор
    tmp3 = str_pat.findall(text2)
    print(tmp3) #['no.', 'yes.']

