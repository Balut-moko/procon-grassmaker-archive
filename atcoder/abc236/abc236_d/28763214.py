from sys import stdin
from collections import deque

readline = stdin.readline
n = int(readline()) * 2
a = [tuple(map(int, readline().split())) for _ in [0] * (n - 1)]


def dfs():
    stack = deque([])
    stack.append([0, 0])
    ans = 0
    while stack:
        bit, joy = stack.pop()
        for j in range(n):
            if not (bit >> j) & 1:
                break
        for k in range(j + 1, n):
            if (bit >> k) & 1:
                continue
            nbit = bit | 1 << j | 1 << k
            njoy = joy ^ a[j][k - j - 1]
            if nbit + 1 == 1 << n:
                ans = max(ans, njoy)
            else:
                stack.append([nbit, njoy])
    return ans


print(dfs())
