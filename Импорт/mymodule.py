import math
import import_my
from math import *

NAME = "mymodule глобальная переменная"

def floor(x):
    print("функция floor из mymodule")
    return x


#print(__name__)

# if __name__ == '__main__':
#     for i in range(4):
#         print(NAME)

print(NAME)