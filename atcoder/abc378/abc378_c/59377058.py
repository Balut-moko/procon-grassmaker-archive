from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

di = defaultdict(lambda: -1)
B = []
for i, a in enumerate(A):
    B.append(di[a])
    di[a] = i + 1

print(*B)
