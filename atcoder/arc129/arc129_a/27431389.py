from sys import stdin

readline = stdin.readline
n, left, right = map(int, readline().split())
ans = 0
for i in range(61):
    if 2**i ^ n < n:
        if left < 2**i and 2**i <= right:
            ans += 2**(i + 1) - 2**i
        if 2**i <= left < 2 ** (i + 1):
            ans += 2**(i + 1) - left
        if 2**i <= right < 2 ** (i + 1):
            ans -= 2**(i + 1) - 1 - right
print(ans)
