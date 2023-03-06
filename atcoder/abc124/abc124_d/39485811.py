from sys import stdin
from itertools import groupby

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
p = 0

left = 0
right = len(rle)

for i in range(len(rle)):
    if rle[i][0] == "0":
        if k > 0:
            p += rle[i][1]
            k -= 1
        else:
            right = i - 1
            break
    if rle[i][0] == "1":
        p += rle[i][1]

ans = p
while right < len(rle):
    if rle[left][0] == "0":
        p -= rle[left][1]
        left += 1
        right += 1
        while right < len(rle):
            if rle[right][0] == "0":
                p += rle[right][1]
                right += 1
            else:
                p += rle[right][1]
                break
    else:
        p -= rle[left][1]
        left += 1
    ans = max(ans, p)
print(ans)
