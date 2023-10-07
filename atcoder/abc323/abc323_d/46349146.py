from heapq import heapify, heappop, heappush

N = int(input())
hq = [tuple(map(int, input().split())) for _ in [0] * N]
heapify(hq)
ans = 0
while hq:
    s, c = heappop(hq)
    while hq:
        if hq[0][0] == s:
            s1, c1 = heappop(hq)
            c += c1
        else:
            break
    if c == 1:
        ans += 1
        continue
    if c % 2 == 1:
        ans += 1
    heappush(hq, (s * 2, c // 2))

print(ans)
