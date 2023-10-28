from collections import deque


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
x = A[0]
q = deque()
for val in A:
    q.append(val)
    while q and not (val < x + M):  # (満たすべき条件)
        rm = q.popleft()
        x = q[0]
    ans = max(ans, len(q))

print(ans)
