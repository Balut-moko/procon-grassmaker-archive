from sys import stdin
from itertools import groupby


def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


readline = stdin.readline
n = int(readline())
s = readline()[:-1]
rle = runLengthEncode(s)
ans = 0
for _, cnt in rle:
    if cnt > 1:
        ans += cnt * (cnt - 1) // 2
print(ans)
