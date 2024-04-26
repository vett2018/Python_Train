import re
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

if __name__ == '__main__':

    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.replace('yeah', 'YYYY')) #YYYY, but no, but YYYY, but no, but YYYY

    text2 = 'Today is 11/27/2012. PyCon starts 12/3/2013.'

    tmp = re.sub(r'(\d+)/(\d+)/(\d+)', r'\1-\2-\3', text2)
    print(tmp)

    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.sub(r'\1-\2-\3', text2))
    print("+++++++++++++++++++++++++++++++++++++++++++++++")


    #tmp2 = datepat.sub(change_date, text2)
    tmp2 = datepat.sub(change_date, text2)

    print(tmp2)

    newtext, n = datepat.subn(r'\3-\1-\2', text2)
    print(newtext)
    print(n)






