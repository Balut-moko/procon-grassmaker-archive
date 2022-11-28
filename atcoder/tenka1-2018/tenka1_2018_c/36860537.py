from sys import stdin

readline = stdin.readline
n = int(readline())
a = [int(readline()) for _ in [0] * n]
a.sort()
small = a[: n // 2]

if n % 2 == 0:
    large = a[n // 2 :]
    ans = 2 * sum(large) - 2 * sum(small)
    ans -= large[0] - small[-1]
else:
    large = a[n // 2 + 1 :]
    mid = a[n // 2]

    tmp = 2 * sum(large) - 2 * sum(small)
    ans = tmp + mid - large[0]
    tmp += -mid + small[-1]
    ans = max(ans, tmp)
print(ans)
