from sys import stdin

readline = stdin.readline
n = int(readline())
a = [int(readline()) for _ in [0] * n]
ans = "second"
for val in a:
    if val % 2 == 1:
        ans = "first"
print(ans)
