

if __name__ == '__main__':
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print(type(parts))
    print(type(' '.join(parts)))
    print(' '.join(parts))
    print(','.join(parts))
    print("".join(parts))
    a = 'Is Chicago'
    b = 'Not Chicago?'
    print('{} - {}'.format(a, b))

    s = ''
    for p in parts:
        s += p
    print('s = ',s)

    tmp = ' '.join(str(d) for d in parts)
    print(tmp)

    # s2 = ''
    # for t in parts:
    #     s2.join(str(t))
    # #print("s2", s2)