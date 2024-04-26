import re

if __name__ == '__main__':
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/* this is a
     multiline comment */
     '''
    tmp = comment.findall(text1)
    print(tmp)
    comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
    tmp2 = comment2.findall(text2)
    print(tmp2)
    comment3 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    tmp3 = comment3.findall(text2)
    print(tmp3)
    print("++++++++++++++++++")
    print(re.compile(r'/\*(.*?)\*/', re.DOTALL).findall(text2))

