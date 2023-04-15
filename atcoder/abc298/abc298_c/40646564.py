from collections import defaultdict
from sys import stdin

readline = stdin.readline
N = int(readline())
Q = int(readline())

dic = defaultdict(list)
dic_box = defaultdict(set)
for _ in range(Q):
    t, *ij = map(int, readline().split())

    if t == 1:
        i, j = ij
        dic[j].append(i)
        dic_box[i].add(j)
    if t == 2:
        ans = sorted(dic[ij[0]])
        print(*ans)
    if t == 3:
        ans = sorted(dic_box[ij[0]])
        print(*ans)
