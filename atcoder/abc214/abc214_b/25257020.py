from sys import stdin

readline = stdin.readline
s, t = map(int, readline().split())
ans = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i + j + k <= s and i * j * k <= t:
                ans += 1
print(ans)
