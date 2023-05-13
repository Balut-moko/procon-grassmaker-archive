from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
ans = []
ans.append(a[0])
for i in range(n - 1):
    if a[i] < a[i + 1]:
        ans = ans + list(range(a[i] + 1, a[i + 1]))
        ans.append(a[i + 1])
    else:
        ans = ans + list(range(a[i] - 1, a[i + 1], -1))
        ans.append(a[i + 1])
print(*ans)
