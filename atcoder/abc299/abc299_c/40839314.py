import itertools
from sys import stdin


def runLengthEncode(s):
    return [(k, len(list(v))) for k, v in itertools.groupby(s)]


readline = stdin.readline
n = int(readline())
s = readline()[:-1]

if s.count("o") == n or s.count("-") == n:
    print(-1)
    exit()

rle = runLengthEncode(s)
ans = 0
for k, v in rle:
    if k == "o":
        ans = max(ans, v)
print(ans)
