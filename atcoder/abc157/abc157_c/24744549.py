from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
sc = [list(map(int, readline().split())) for _ in range(m)]
if n == 1:
    start = 0

else:
    start = 10 ** (n - 1)

ans = -1
for i in range(start, 10**n):
    tmp = str(i)
    for val in sc:
        if tmp[val[0]-1] != str(val[1]):
            break
    else:
        ans = i
        break

print(ans)
