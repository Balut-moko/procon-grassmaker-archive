from sys import stdin


def int1(x):
    return int(x) - 1


readline = stdin.readline
n = int(readline())
a = list(map(int1, readline().split()))
ans = 0
for i in range(n):
    if i == a[a[i]]:
        ans += 1
print(ans // 2)
