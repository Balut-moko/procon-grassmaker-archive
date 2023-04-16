from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
ans = []
for i in range(1, n + 1):
    x = i
    x = a[i - 1]
    j = 1
    while x != i:
        x = a[x - 1]
        j += 1
    ans.append(j)
print(*ans)
