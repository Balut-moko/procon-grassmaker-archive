from sys import stdin
import re

readline = stdin.readline
s = readline()[:-1]
print(re.sub("[aiueo]", "", s))
