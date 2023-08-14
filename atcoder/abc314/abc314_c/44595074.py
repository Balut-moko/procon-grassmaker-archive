from collections import defaultdict, deque
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = readline()[:-1]
a = list(map(int, readline().split()))

dique = defaultdict(deque)

for i in range(n):
    dique[a[i]].append(s[i])

for i in range(1, m + 1):
    v = dique[i].pop()
    dique[i].appendleft(v)

ans = []
for i in range(n):
    ans.append(dique[a[i]].popleft())

print(*ans, sep="")
