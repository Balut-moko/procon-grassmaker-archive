from collections import deque
from itertools import permutations
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]
t = {readline()[:-1] for _ in [0] * m}

for val in permutations(s):
    que1 = deque([val[0]])
    que2 = deque([])
    i = 1
    while i < n:
        while que1:
            q = que1.popleft()
            for j in range(1, 14):
                tmp = q + "_" * j + val[i]
                if len(tmp) > 16:
                    break
                que2.append(tmp)
        que1, que2 = que2, que1
        i += 1

    st = set(que1) - t
    for ans in st:
        if 3 <= len(ans):
            print(ans)
            exit()
print(-1)
