from collections import Counter
from sys import stdin

readline = stdin.readline
s = readline()[:-1]
cnt = Counter(s)

print(cnt.most_common()[0][0])
