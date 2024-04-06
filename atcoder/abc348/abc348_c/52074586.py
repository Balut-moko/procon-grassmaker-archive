from collections import defaultdict


N = int(input())
di = defaultdict(lambda: 1 << 60)
for i in range(N):
    A, C = map(int, input().split())
    di[C] = min(di[C], A)

print(max(di.values()))
