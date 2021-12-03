from sys import stdin

readline = stdin.readline
n = int(readline())
ans = 0
for i in range(n + 1):
    if i * i <= n:
        k = i
    else:
        break
for i in range(1, k + 1):
    ans += ((n // i) - (n // (i + 1))) * i
for i in range(1, n // (k + 1) + 1):
    ans += n // i

print(ans)
