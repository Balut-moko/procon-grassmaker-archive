from sys import stdin
import re

readline = stdin.readline
print(re.sub("[aiueo]", "", readline()[:-1]))
