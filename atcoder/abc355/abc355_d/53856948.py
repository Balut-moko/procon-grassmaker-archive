from heapq import heappop, heappush


N = int(input())
LR = [tuple(map(int, input().split())) for _ in [0] * N]

cnt = 0
ans = 0
hq = []

for l, r in LR:
    heappush(hq, (l, 1))
for l, r in LR:
    heappush(hq, (r, 2))

while hq:
    _, c = heappop(hq)
    if c == 2:
        cnt -= 1
        ans += cnt
    else:
        cnt += 1

print(ans)
