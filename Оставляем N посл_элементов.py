from collections import deque


# простое сопоставление текста с
# последовательностью строк,
# а при совпадении выдает совпавшие строки вместе с N предыдущими строками контекста
def search(lines, pattern, history=777):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'language', 777):
            for pline in prevlines:
                print(pline, end=" ")
            print(line, end="")
            print('-' * 20)
