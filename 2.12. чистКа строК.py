import re
import unicodedata, sys

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

if __name__ == '__main__':
    str_ = 'ПриВет, Я Из ГоРоДа СаНкТ-ПеТеРбУрг'
    print(str_)
    print(str_.upper())
    print(str_.lower())
    print(str_.replace("СаНкТ-ПеТеРбУрг", "Москва"))
    str_ = unicodedata.normalize ('NFC', str_) #yнормализация текста
    tmp2 = re.sub('СаНкТ-ПеТеРбУрг', matchcase('Нижний Новгород'), str_, flags=re.IGNORECASE)
    print(tmp2)
    print('+++++++++++++++++++++++++++++')
    """
    
    """
    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(s)
    remap = {
        ord('\t') : ' ',
        ord('\f') : ' ',
        ord('\r') : None #Удален
    }
    a = s.translate(remap)
    print(a)
    print('__________')
    """
    """
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    print(cmb_chrs)
    b = unicodedata.normalize('NFD', a)
    print(b)
    tmp3 = b.translate(cmb_chrs)
    print(tmp3)
    print("+++++++++++"
          "+++++++++++")
    """
     пример – таблица перевода, которая отображает все десятичные цифры Unicode на их эквиваленты в ASCII: 
    """

    digitmap = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if
                unicodedata.category(chr(c)) == 'Nd'}

    print(digitmap)
    """
    переписал dictcomprehesion
    """
    print("____________________________________")
    digitmap2 = {}
    for c in range(sys.maxunicode):
        if unicodedata.category(chr(c)) == 'Nd':
            dict_ = {c: ord('0') + unicodedata.digit(chr(c))}
            digitmap2.update(dict_)
    print(digitmap2)

    print(len(digitmap2))
    # Арабские цифры
    x = '\u0661\u0662\u0663\u0664\u0665'
    print(x)
    print(x.translate(digitmap2))
    print('++++++++++++++++++++++')
    print(a)
    print(unicodedata.normalize('NFD', a).encode('ascii', 'ignore').decode('ascii'))