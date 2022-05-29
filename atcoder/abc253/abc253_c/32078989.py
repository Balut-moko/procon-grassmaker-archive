from collections import defaultdict
from bisect import insort_left
from sys import stdin

readline = stdin.readline
q = int(readline())
di = defaultdict(int)
li = []
num_set = set()

for _ in range(q):
    que = tuple(map(int, readline().split()))
    if que[0] == 1:
        di[que[1]] += 1
        num_set.add(que[1])
        if di[que[1]] == 1:
            insort_left(li, que[1])
    elif que[0] == 2:
        di[que[1]] -= min(que[2], di[que[1]])
        if di[que[1]] == 0:
            if que[1] in num_set:
                num_set.remove(que[1])
                li.remove(que[1])
    else:
        print(li[-1] - li[0])
