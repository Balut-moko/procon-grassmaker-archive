from itertools import permutations
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]

for val in permutations(s):
    for i in range(n - 1):
        cnt = 0
        for j in range(m):
            if val[i][j] != val[i + 1][j]:
                cnt += 1
        if cnt != 1:
            break
    else:
        print("Yes")
        exit()
print("No")
