from sys import stdin

readline = stdin.readline
n = int(readline())
s = [set(list(readline()[:-1])) for _ in [0] * n]
ans = [""] * n
for i in range(n // 2):
    s_i = s[i] & s[n - 1 - i]
    if s_i:
        val = s_i.pop()
        ans[i] = val
        ans[n - 1 - i] = val
    else:
        print(-1)
        exit()

if n % 2 == 1:
    ans[(n - 1) // 2] = s[(n - 1) // 2].pop()

print(*ans, sep="")
