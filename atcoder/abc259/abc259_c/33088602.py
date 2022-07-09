from sys import stdin
from itertools import groupby


def runLengthEncode(S):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


readline = stdin.readline
s = readline()[:-1]
t = readline()[:-1]

s_rle = runLengthEncode(s)
t_rle = runLengthEncode(t)

if len(s_rle) != len(t_rle):
    print("No")
    exit()

for i in range(len(s_rle)):
    if s_rle[i][0] != t_rle[i][0]:
        break
    if s_rle[i][1] == 1 and t_rle[i][1] == 1:
        continue
    if s_rle[i][1] == 1:
        break
    if s_rle[i][1] > t_rle[i][1]:
        break
else:
    print("Yes")
    exit()
print("No")
