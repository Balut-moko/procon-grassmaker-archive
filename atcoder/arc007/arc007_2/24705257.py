from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
ans = list(range(1, n + 1))
tmp = 0
for _ in range(m):
    disk = int(readline())
    if tmp == disk:
        continue
    tmp, ans[ans.index(disk)] = ans[ans.index(disk)], tmp
print(*ans, sep='\n')
