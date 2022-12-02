from sys import stdin

readline = stdin.readline
n = int(readline())
ans = 0
ans = 0
for i in range(1, 10**6 + 1):
    tmp = n
    tmp -= i
    m = tmp // i
    if m > 0 and n // m == n % m:
        ans += m
print(ans)
