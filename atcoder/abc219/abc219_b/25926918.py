from sys import stdin

readline = stdin.readline
s = [readline()[:-1] for _ in [0] * 3]
t = list(map(int, readline()[:-1]))
ans = ''
for val in t:
    ans += s[val - 1]
print(ans)
