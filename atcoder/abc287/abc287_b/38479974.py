from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]
t = [readline()[:-1] for _ in [0] * m]
ans = 0
for val in s:
    if val[-3:] in t:
        ans += 1

print(ans)
