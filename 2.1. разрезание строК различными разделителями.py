import re

if __name__ == '__main__':
    line = 'asdf fjdk; afed, fjek,asdf,      foo'
    print(line)
    line2 = re.split(r'(;,\s)\s*', line)
    line3 = re.split(r'[;,\s]\s*', line)
    print(line2)
    print(line3)
    print('______________________________')
    fields = re.split(r'(;|,|\s)\s*', line)
    print('1= ',fields)
    values = fields[::2]
    delimiters = fields[1::2] + ['']
    print(delimiters)
    print(values)
    print('______________________________')
    # Переформатируем строку, используя те же разделители >>>
    line4 = ''.join(v+d for v, d in zip(values, delimiters))
    print(line4)

    print('______________________________')
    """
     чтобы разделители попали в результат, но при этом вам 
     нужно применить группы в шаблоне регулярного выражения, 
     убедитесь, что вы используете незахватывающую (noncapture) группу
    """
    line5 = re.split(r'(?:,|;|\s)\s*', line)
    print(line5)

