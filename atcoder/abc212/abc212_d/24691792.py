from sys import stdin
import heapq

readline = stdin.readline
Q = int(readline())
plus_num = 0
ans = []
balls = []
heapq.heapify(balls)

for _ in range(Q):
    q = list(map(int, readline().split()))
    if q[0] == 1:
        heapq.heappush(balls, q[1] - plus_num)
    elif q[0] == 2:
        plus_num += q[1]
    else:
        ball = heapq.heappop(balls)
        ans.append(ball + plus_num)
print(*ans, sep='\n')
