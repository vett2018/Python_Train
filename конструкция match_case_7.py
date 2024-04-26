CMD_3 = 3
CMD_5 = 5
"""
Целочисленная переменная. Выделить две ситуации со значением 3 и значением 5
"""
cmd = 5


match cmd:
    case int() if CMD_3 == cmd: # int(cmd) as x if x == CMD_3:
        print("3")
    case int(cmd) as x if x == CMD_5:
        print("5")
    case _:
        print("другое")