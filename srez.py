if __name__ == '__main__':
    ###### 0123456789012345678901234567890123456789012345678901234567890'
    record = '....................100 .......513.25 ..........'
    print(record)
    SHARES = slice(20, 32)
    PRICE = slice(40, 48)
    cost = record[SHARES] * record[PRICE]