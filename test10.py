with open('test10.txt', 'wt', encoding='utf-8') as infile:
    num = int(input('введите число '))
    line = str('1 / ' + str(num) + " = " + str(1 / num))
    print(line)
    infile.write(line)