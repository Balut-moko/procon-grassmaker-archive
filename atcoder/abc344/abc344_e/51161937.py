N = int(input())
A = list(map(int, input().split()))
A = [0] + A + [-1]
prev = {}
nxt = {}
for i in range(N + 1):
    prev[A[i + 1]] = A[i]
    nxt[A[i]] = A[i + 1]

Q = int(input())
for _ in range(Q):
    c, *a = map(int, input().split())
    if c == 1:
        x, y = a
        n = nxt[x]
        nxt[x] = y
        prev[y] = x
        nxt[y] = n
        prev[n] = y
    else:
        x = a[0]
        p = prev[x]
        n = nxt[x]
        prev[n] = p
        nxt[p] = n

ans = []
cur = nxt[0]
while cur != -1:
    ans.append(cur)
    cur = nxt[cur]
print(*ans)
