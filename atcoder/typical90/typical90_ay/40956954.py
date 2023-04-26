from bisect import bisect_right
from sys import stdin


def has_bit(n, i):
    return n & (1 << i) > 0


readline = stdin.readline
N, K, p = map(int, readline().split())
a = list(map(int, readline().split()))


def bitAllSearch(N, aa):
    res = [[] for _ in [0] * (K + 1)]
    for n in range(2 ** N):
        cnt = 0
        cost = 0
        for i in range(N):
            if has_bit(n, i):
                cnt += 1
                cost += aa[i]
        if cnt <= K and cost <= p:
            res[cnt].append(cost)

    for k in range(K + 1):
        res[k] = sorted(res[k])
    return res


left = bitAllSearch(N // 2, a[: N // 2])
right = bitAllSearch(N - N // 2, a[N // 2 :])

ans = 0
for k in range(K + 1):
    for l_ans in left[k]:
        ans += bisect_right(right[K - k], p - l_ans)

print(ans)
