from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
a = list(map(lambda x: int(x) - 1, readline().split()))
flg = [False] * n
flg[x - 1] = True
tmp = x - 1
while True:
    if not flg[a[tmp]]:
        flg[a[tmp]] = True
        tmp = a[tmp]
    else:
        break
print(sum(flg))
