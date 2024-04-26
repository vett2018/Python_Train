"""
Регулярные выражения
"""

import re

if __name__ == '__main__':
    text1 = '11/27/2012'
    print(re.match(r'\d+/\d+/\d+', text1))
    text2 = 'Nov 27, 2012'

    # Простое сопоставление: \d+ означает совпадение одной или более цифр
    if re.match(r'\d+/\d+/\d+', text1):
        print("yes")
    else:
        print("no")

    datepat = re.compile(r'\d+/\d+/\d+') # использование шаблона многократно
    if datepat.match(text1):
        print("yes")
    else:
        print("no")

    text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print(datepat.findall(text3))

    datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat2.findall(text3))

    # Извлекаем содержимое каждой группы
    m = datepat2.match('11/27/2012')
    print(m) #<re.Match object; span=(0, 10), match='11/27/2012'>
    print(m.group(1)) #11
    print(m.groups()) #('11', '27', '2012')

    print("_____________________________________________-")
    datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
    # Найти все совпадения (обратите внимание на разрезание на кортежи)

    text4 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print(datepat2.findall(text4)) #[('11', '27', '2012'), ('3', '13', '2013')]
    print("______")
    for month, day, year in datepat2.findall(text4):
        print('{}--{}--{}'.format(year, month, day)) #2012--11--27
                                                     #2013--3--13

    print("____________")
    for m in datepat2.finditer(text4):
        print(m.groups())   #('11', '27', '2012')
                            #('3', '13', '2013')
