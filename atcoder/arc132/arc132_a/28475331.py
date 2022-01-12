from sys import stdin

readline = stdin.readline
n = int(readline())
r = list(map(int, readline().split()))
c = list(map(int, readline().split()))
q = int(readline())
rc = [tuple(map(int, readline().split())) for _ in [0] * q]
ans = ''
for i, j in rc:
    if n - r[i - 1] < c[j - 1]:
        ans += '#'
    else:
        ans += '.'
print(ans)
