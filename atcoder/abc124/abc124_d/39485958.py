from sys import stdin
from itertools import groupby
from collections import deque

readline = stdin.readline
n, k = map(int, readline().split())
s = readline()[:-1]


def runLengthEncode(s):
    grouped = groupby(s)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


rle = runLengthEncode(s)

cnt = 0
ans = 0
tmp = 0

q = deque()
for val in rle:
    q.append(val)
    # 追加した要素に応じた処理
    tmp += val[1]
    if val[0] == "0":
        cnt += 1
    while q and not (cnt <= k):  # (満たすべき条件)
        rm = q.popleft()
        # 取り除いた要素に応じた処理
        tmp -= rm[1]
        if rm[0] == "0":
            cnt -= 1
    # 何らかの処理 右端の要素から左に延ばせる最大の長さ
    ans = max(ans, tmp)

print(ans)
