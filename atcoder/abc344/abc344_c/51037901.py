from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

ans = defaultdict(bool)

for a in A:
    for b in B:
        for c in C:
            ans[a + b + c] = True

for x in X:
    print("Yes" if ans[x] else "No")
