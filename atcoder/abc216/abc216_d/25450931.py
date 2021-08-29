from sys import stdin
from collections import deque


def int1(x): return int(x) - 1


readline = stdin.readline
n, m = map(int, readline().split())
ans = 'Yes'
stack = []
que = deque([])
cnt = [[] for _ in range(n)]
for i in range(m):
    k = int(readline())
    tmp = deque(map(int1, readline().split()))
    cnt[tmp[0]].append(i)
    stack.append(tmp)
for i in range(n):
    if len(cnt[i]) == 2:
        que.append(i)
while que:
    q = que.pop()
    for c in cnt[q]:
        stack[c].popleft()
        if 0 < len(stack[c]):
            cnt[stack[c][0]].append(c)
            if len(cnt[stack[c][0]]) == 2:
                que.append(stack[c][0])
for s in stack:
    if 0 < len(s):
        ans = 'No'
print(ans)
