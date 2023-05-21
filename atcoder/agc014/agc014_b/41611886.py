from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
cnt = [0] * n
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    if a > b:
        a, b = b, a
    cnt[a] += 1
    cnt[b] -= 1
flg = True
for i in range(n - 1):
    cnt[i + 1] += cnt[i]
    if cnt[i] % 2 != 0:
        flg = False

print("YES" if flg else "NO")
