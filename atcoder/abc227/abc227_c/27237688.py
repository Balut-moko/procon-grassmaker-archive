from sys import stdin

readline = stdin.readline
n = int(readline())
ans = 0
for a in range(1, 5000):
    tmp = n // a
    for b in range(a, 10**6):
        if b * b > tmp:
            break
        ans += (tmp // b) - b + 1
print(ans)
