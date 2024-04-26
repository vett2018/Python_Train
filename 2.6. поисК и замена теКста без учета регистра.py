import re

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
    text = 'UPPER PYTHON, lower Sython, Mixed Python'
    tmp = re.findall('python', text, flags=re.IGNORECASE)
    print(tmp) #['PYTHON', 'python', 'Python']
    print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print(text)
    tmp2 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
    print(tmp2) #UPPER snake, lower snake, Mixed snake
    print("++++++++++++++++++++++++++++++++++++++++++++++++")

    #tmp3 = re.sub('python', matchcase('Snake'), text, flags=re.IGNORECASE)
    tmp3 = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
    print(tmp3) #UPPER SNAKE, lower snake, Mixed Snake



