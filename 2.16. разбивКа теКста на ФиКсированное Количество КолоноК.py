import textwrap, os

if __name__ == '__main__':
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, the eyes, " \
        "not around the eyes, don't look around the eyes, look into my eyes, " \
        "you're under."
    print(s)
    print('1++++++++++++++++++')
    print(textwrap.fill(s, 70))
    print('2++++++++++++++++++')
    print(textwrap.fill(s, 40))
    print('3++++++++++++++++++')
    print(textwrap.fill(s, 40, initial_indent=' '))
    print('4++++++++++++++++++')
    print(textwrap.fill(s, 40, subsequent_indent=' '))
