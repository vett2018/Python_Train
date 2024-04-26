from html.parser import HTMLParser
import html, re
from collections import namedtuple


if __name__ == '__main__':
    expr ::= expr + term | expr - term | term
    term ::= term * factor | term / factor | factor
    factor ::= (expr) | NUM
    expr: := term {(+ | -) term} *




