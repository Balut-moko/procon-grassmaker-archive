from collections import Counter


N = int(input())
A = list(map(int, input().split()))
flag = 0
for i in range(N):
    flag ^= A[i]

if flag != 0:
    print(-1)
    exit()

cnt = Counter(A)
A.sort(reverse=True)
for a in A:
    if cnt[a] % 2 == 1:
        print(a - 1)
        exit()

print(0)
