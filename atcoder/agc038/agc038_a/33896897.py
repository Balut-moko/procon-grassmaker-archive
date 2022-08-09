from sys import stdin

readline = stdin.readline
h, w, a, b = map(int, readline().split())
ans = []
for r in range(h):
    if r < b:
        ans.append("0" * a + "1" * (w - a))
    else:
        ans.append("1" * a + "0" * (w - a))
for val in ans:
    print(val)
