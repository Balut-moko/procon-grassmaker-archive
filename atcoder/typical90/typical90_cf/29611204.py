from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
ans = n * (n + 1) // 2
now = ""
cnt = 0
for val in s:
    if val == now:
        cnt += 1
    else:
        ans -= cnt * (cnt + 1) // 2
        now = val
        cnt = 1

ans -= cnt * (cnt + 1) // 2

print(ans)
