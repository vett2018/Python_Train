import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape


if __name__ == '__main__':
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)
    print(html.escape(s))
    # Отключим экранирование кавычек
    print(html.escape(s, quote = False))
    print('+++++++++++++++++++++++++++')
    del s
    s = 'Spicy Jalapeño'
    tmp2 = s.encode('ascii', errors='xmlcharrefreplace')
    print(tmp2)
    del s
    s = 'Spicy &quot;Jalape&#241;o&quot.'
    p = HTMLParser()




