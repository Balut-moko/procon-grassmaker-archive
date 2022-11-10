from itertools import groupby
from sys import stdin


def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        cnt = len(list(v))
        res.append((k, cnt))
    return res


readline = stdin.readline
n, k = map(int, readline().split())
s = readline()[:-1]
rle = runLengthEncode(s)
cnt = len(rle)
for _ in range(k):
    if cnt >= 3:
        cnt -= 2
    elif cnt == 2:
        cnt -= 1
print(n - cnt)
