from sys import stdin

readline = stdin.readline
n = int(readline())
ans = 0
for a in range(1, n):
    for b in range(1, n):
        if a * b < n:
            ans += 1
        else:
            break
print(ans)