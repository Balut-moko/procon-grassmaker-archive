from sys import stdin
import re


def func_repl(matched):
    s = matched.group(0)
    return s[1:] + s[0]


readline = stdin.readline
n = int(readline())
s = s1 = readline()[:-1]
s1 = s1.replace("BB", "A")
s1 = re.sub(r"BA+", func_repl, s1)

while s != s1:
    s = s1
    s1 = s1.replace("BB", "A")
    s1 = re.sub(r"BA+", func_repl, s1)
print(s1)
