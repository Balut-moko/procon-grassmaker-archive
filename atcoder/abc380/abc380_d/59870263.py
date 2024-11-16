S = input()
Q = int(input())
K = list(map(int, input().split()))
M = len(S)

#  0 -> S
#  1 -> T
T = "".join([s.upper() if s.islower() else s.lower() for s in S])

ans = [None] * Q

for i, k in enumerate(K):
    block, idx = divmod(k, M)
    if idx == 0:
        block -= 1
        idx = M
    cnt = 0
    while block > 0:
        c = 0
        b = block
        while b > 0:
            b //= 2
            c += 1
        block -= 1 << (c - 1)
        cnt += 1

    if cnt % 2 == 0:
        ans[i] = S[idx - 1]
    else:
        ans[i] = T[idx - 1]

print(*ans)
